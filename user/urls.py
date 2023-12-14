from django.urls import path
from .views import UserCreateView, UserDetailView, ChangePasswordView

urlpatterns = [
    path("signup/", UserCreateView.as_view(), name="signup"),
    path("user/<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    path("password/change/", ChangePasswordView.as_view(), name="change_password"),
]
