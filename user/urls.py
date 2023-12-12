from django.urls import path
from .views import (
    UserCreateView
    UserDetailVIew
)

urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='signup'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    
]
