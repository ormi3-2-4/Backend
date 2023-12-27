from django.urls import path, include
from rest_framework.routers import DefaultRouter
from community.views import CommunityCommentView, CommunityView

community_router = DefaultRouter()
community_router.register("", CommunityView, basename="community")

community_comment_router = DefaultRouter()
community_comment_router.register(
    "",
    CommunityCommentView,
    basename="community-comment",
)


urlpatterns = [
    path("comments/", include(community_comment_router.urls)),
    path("", include(community_router.urls)),
]
