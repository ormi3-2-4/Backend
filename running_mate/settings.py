from datetime import timedelta
from datetime import timedelta
from os import getenv
from pathlib import Path

import environ
import pymysql

pymysql.install_as_MySQLdb()

env = environ.Env(DEBUG=(bool, True))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(BASE_DIR / ".env")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = getenv("DEBUG")

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # third-party
    "rest_framework",
    "rest_framework_simplejwt",
    "drf_spectacular",
    "storages",
    # local
    "record",
    "course",
    "community",
    "recommend",
    "user",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "running_mate.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI_APPLICATION = "running_mate.asgi.application"
ASGI_APPLICATION = "running_mate.asgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": getenv("DB_NAME") if DEBUG else getenv("DB_REMOTE_NAME"),
        "USER": getenv("DB_USER") if DEBUG else getenv("DB_REMOTE_USERNAME"),
        "PASSWORD": getenv("DB_PW") if DEBUG else getenv("DB_REMOTE_PW"),
        "HOST": getenv("DB_HOST") if DEBUG else getenv("DB_REMOTE_HOST"),
        "PORT": getenv("DB_PORT") if DEBUG else getenv("DB_REMOTE_PORT"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# dj-rest-auth
REST_USE_JWT = True  # JWT 사용 여부
JWT_AUTH_COOKIE = "my-app-auth"  # 호출할 Cookie Key 값
JWT_AUTH_REFRESH_COOKIE = "my-refresh-token"  # Refresh Token Cookie Key 값

# django-allauth
SITE_ID = 1  # 해당 도메인 id
ACCOUNT_UNIQUE_EMAIL = True  # User email unique 사용 여부
ACCOUNT_USER_MODEL_USERNAME_FIELD = "email"  # 사용자 이름 필드 지정
ACCOUNT_USERNAME_REQUIRED = False  # User username 필수 여부
ACCOUNT_EMAIL_REQUIRED = True  # User email 필수 여부
ACCOUNT_AUTHENTICATION_METHOD = "email"  # 로그인 인증 수단
ACCOUNT_EMAIL_VERIFICATION = "none"  # email 인증 필수 여부

# JWT
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),  # AccessToken 유효 기간 설정
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(weeks=12),  # RefreshToken 유효 기간 설정
    "USER_ID_FIELD": "pk",
    "USER_ID_CLAIM": "user_id",
}

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

# drf-spectacular
SPECTACULAR_SETTINGS = {
    "TITLE": "schema",
    "DESCRIPTION": "운동 기록을 공유하는 SNS 서비스",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": True,
    # OTHER SETTINGS
}
AUTH_USER_MODEL = "user.User"

# AWS
AWS_ACCESS_KEY_ID = getenv("S3_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = getenv("S3_SECRET_ACCESS_KEY")
AWS_REGION = "ap-northeast-2"

# S3
AWS_STORAGE_BUCKET_NAME = getenv("BUCKET_NAME")
S3_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com"
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"
