from django.urls import path, include
from rest_framework import routers
from record.views import RecordViewSet, LeafletView

router = routers.DefaultRouter()
router.register("", RecordViewSet)

urlpatterns = [
    path("maps/<int:pk>/", LeafletView.as_view(), name="maps"),
    path("", include(router.urls)),
]