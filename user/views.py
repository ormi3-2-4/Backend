from django.contrib.auth import get_user_model
from django.http import Http404, HttpRequest
from rest_framework import permissions, generics
from rest_framework.generics import get_object_or_404, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
)
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from user.serializers import (
    UserLoginSerializer,
    UserSerializer,
    ChangePasswordSerializer,
    UserUpdateSerializer,
)

User = get_user_model()


class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]
    http_method_names = ["post"]

    def post(self, request: HttpRequest):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.filter(email=serializer.data["email"]).first()
            if not user:
                return Response("유저가 존재하지 않습니다.", HTTP_404_NOT_FOUND)

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


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ChangePasswordView(APIView):
    permission_classes = [permissions.IsAuthenticated]

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


class UserUpdateView(RetrieveUpdateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserUpdateSerializer

    def get_object(self):
        return self.request.user
