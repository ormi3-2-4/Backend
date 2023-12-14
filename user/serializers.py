from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(allow_null=True, required=False)

    class Meta:
        model = User
        fields = ("id", "email", "password", "nickname", "profile_image")
        extra_kwargs = {"password": {"write_only": True}}
        read_only_fields = ["id"]

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            return user


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ("email", "password")
