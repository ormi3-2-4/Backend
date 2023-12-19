from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, nickname, email, password):
        if not email:
            raise ValueError("이메일은 필수입니다.")
        email = self.normalize_email(email)
        user = self.model(
            nickname=nickname,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nickname, email, password):
        user: User = self.create_user(
            nickname=nickname,
            email=self.normalize_email(email),
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True, help_text="이메일")
    nickname = models.CharField(max_length=20, help_text="닉네임")
    profile_image = models.ImageField(blank=True, upload_to="user/images", null=True)
    password = models.CharField(_("password"), max_length=128)
    joined_at = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["nickname"]

    class Meta:
        db_table = "user"
        verbose_name = "유저"
        verbose_name_plural = "유저"

    def __str__(self):
        return self.nickname

    def has_perm(self, perm, obj=None):
        return True
    
    def has_perms(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
