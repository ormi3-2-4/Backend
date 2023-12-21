from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommunityView, CommunityCommentView

router = DefaultRouter()
router.register(r'community', CommunityView, basename='community')
router.register(r'community/(?P<community_pk>\d+)/comments/', CommunityCommentView, basename='community-comment')


urlpatterns = [
    path('api/', include(router.urls)),
]