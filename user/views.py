from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import permissions, status
from .serializers import UserSerializer, ChangePasswordSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


User = get_user_model()


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


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
            return Response(
                {"detail": "비밀번호가 성공적으로 변경되었습니다."}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
