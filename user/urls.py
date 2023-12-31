from django.urls import path

from user.views import (
    UserLoginView,
    UserRegisterView,
    UserDetailView,
    ChangePasswordView,
)

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("info/", UserDetailView.as_view(), name="user_detail"),
    path(
        "change_password/",
        ChangePasswordView.as_view(),
        name="change_password",
    ),
]
