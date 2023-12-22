from django.contrib.auth import get_user_model
from rest_framework import serializers
from dj_rest_auth.serializers import (
    PasswordResetSerializer as DefaultPasswordResetSerializer,
)

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(allow_null=True, required=False)

    class Meta:
        model = User
        fields = ("id", "email", "password", "nickname", "profile_image")
        extra_kwargs = {"password": {"write_only": True}}
        read_only = ["profile_image"]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError("기존 비밀번호가 올바르지 않습니다.")
        return value

    def save(self, **kwargs):
        user = self.context["request"].user
        new_password = self.validated_data["new_password"]
        user.set_password(new_password)
        user.save()
        return user


class PasswordResetSerializer(DefaultPasswordResetSerializer):
    email = serializers.EmailField()

    def validate_email(self, email):
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("이메일 주소가 올바르지 않습니다.")

        return email


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ("email", "password")


class UserUpdateSerializer(serializers.ModelSerializer):
    profile_image = serializers.FileField(allow_null=True, required=False)
    nickname = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ["nickname", "profile_image"]
