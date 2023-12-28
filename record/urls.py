from django.urls import path, include
from rest_framework import routers
from record.views import RecordViewSet, maps

router = routers.DefaultRouter()
router.register("", RecordViewSet)

urlpatterns = [
    path("maps/<int:pk>/", maps, name="maps"),
    path("", include(router.urls)),
]
