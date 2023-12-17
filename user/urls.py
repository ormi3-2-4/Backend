from django.urls import path
<<<<<<< HEAD
from .views import UserCreateView, UserDetailView, ChangePasswordView

urlpatterns = [
    path("signup/", UserCreateView.as_view(), name="signup"),
    path("user/<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    path("password/change/", ChangePasswordView.as_view(), name="change_password"),
=======

from user.views import UserLoginView, UserRegisterView

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("register/", UserRegisterView.as_view(), name="register"),
>>>>>>> dev
]
