from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('이메일은 필수입니다.')
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            **extra_fields,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)
      
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser는 is_staff=True이어야 합니다.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser는 is_superuser=True이어야 합니다.')
        
        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    nickname = models.CharField(max_length=20)
    profile_image = models.ImageField(blank=True, upload_to='user/images')
    objects = CustomUserManager()
