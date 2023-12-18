from django.urls import path

from user.views import (
    UserLoginView,
    UserRegisterView,
    UserDetailView,
    ChangePasswordView,
    UserUpdateView,
)

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("user/<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    path(
        "user/<int:pk>/change_password/",
        ChangePasswordView.as_view(),
        name="change_password",
    ),
    path("profile/update/", UserUpdateView.as_view(), name="profile_update"),
]
