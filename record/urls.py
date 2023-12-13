from django.urls import path, include
from rest_framework import routers
from record.views import RecordViewSet

router = routers.DefaultRouter()
router.register("", RecordViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
