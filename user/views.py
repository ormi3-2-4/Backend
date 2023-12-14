import json

from django.contrib.auth import get_user_model
from django.http import Http404, HttpRequest
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from common.utils import error_response, success_response
from user.serializers import UserLoginSerializer, UserSerializer

User = get_user_model()


class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]
    http_method_names = ["post"]

    def post(self, request: HttpRequest):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = get_object_or_404(User, email=serializer.data["email"])
            except Http404:
                return error_response("유저가 존재하지 않습니다.", 404)

            token = TokenObtainPairSerializer.get_token(user)
            access_token = str(token.access_token)
            data = {
                "user": serializer.data,
                "token": {
                    "access_token": access_token,
                    "refresh_token": str(token),
                },
            }

            return success_response(data, 200)
        return error_response(serializer.errors, 400)


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
            return success_response(data, 201)
        return error_response(serializer.errors, 400)
