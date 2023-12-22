from django.http import HttpRequest
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
)
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from user.models import User
from drf_spectacular.utils import extend_schema_view, extend_schema
from user.serializers import (
    UserLoginSerializer,
    UserSerializer,
    ChangePasswordSerializer,
    UserUpdateSerializer,
)

class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]
    http_method_names = ["post"]

    @extend_schema(
        description="유저가 로그인을 합니다.",
        request=UserLoginSerializer,
        responses={200: UserSerializer},
    )
    def post(self, request: HttpRequest):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.filter(email=serializer.data["email"]).first()
            if not user:
                return Response("유저가 존재하지 않습니다.", HTTP_404_NOT_FOUND)

            pass_match = user.check_password(serializer.data["password"])
            if not pass_match:
                return Response({"error": "비밀번호가 올바르지 않습니다."}, HTTP_400_BAD_REQUEST)

            token = TokenObtainPairSerializer.get_token(user)
            access_token = str(token.access_token)
            data = {
                "user": UserSerializer(user).data,
                "token": {
                    "access_token": access_token,
                    "refresh_token": str(token),
                },
            }

            return Response(data, HTTP_200_OK)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    http_method_names = ["get", "put"]
    parser_classes = [MultiPartParser]
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        return super().get_queryset().filter(id=self.request.user.id)

    @extend_schema(
        description="유저의 정보를 가져옵니다.",
        request=None,
        responses={200: UserSerializer},
    )
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    @extend_schema(
        description="유저의 정보를 수정합니다.",
        request=UserUpdateSerializer,
        responses={200: UserSerializer},
    )
    def put(self, request: HttpRequest):
        serializer = UserUpdateSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(id=self.request.user.id)
            user.nickname = serializer.validated_data.get("nickname", user.nickname)
            user.profile_image.delete()
            user.profile_image = serializer.validated_data.get(
                "profile_image", user.profile_image
            )
            user.save()
            return Response(UserSerializer(user).data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class ChangePasswordView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        description="유저의 비밀번호를 변경합니다.",
        request=ChangePasswordSerializer,
        responses={200: {"detail": "비밀번호가 성공적으로 변경되었습니다."}},
    )
    def put(self, request):
        serializer = ChangePasswordSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            user = serializer.save()
            return Response({"detail": "비밀번호가 성공적으로 변경되었습니다."}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UserRegisterView(APIView):
    permission_classes = [permissions.AllowAny]
    http_method_names = ["post"]

    @extend_schema(
        description="유저의 정보를 수정합니다.",
        request=UserSerializer,
        responses={200: TokenObtainPairSerializer},
    )
    def post(self, request: HttpRequest):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = TokenObtainPairSerializer.get_token(user)
            access_token = str(token.access_token)
            data = {
                "user": serializer.data,
                "token": {
                    "access_token": access_token,
                    "refresh_token": str(token),
                },
            }
            return Response(data, HTTP_201_CREATED)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)
