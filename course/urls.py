from django.urls import include, path
from rest_framework.routers import DefaultRouter

from course.views import CourseViewSet

router = DefaultRouter()
router.register("", CourseViewSet)
urlpatterns = [
    path("", include(router.urls)),
]
