from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recommend.views import RecommendCommentView, RecommendView

recommend_router = DefaultRouter()
recommend_router.register("", RecommendView, basename="recommend")

recommend_comment_router = DefaultRouter()
recommend_comment_router.register(
    "",
    RecommendCommentView,
    basename="recommend-comment",
)


urlpatterns = [
    path("", include(recommend_router.urls)),
    path("comments/", include(recommend_comment_router.urls)),
]
