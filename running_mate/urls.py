from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from record.models import Record
from djgeojson.views import GeoJSONLayerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("user.urls")),
    path('record/', include('record.urls')),
    path('maps/<int:pk>/', TemplateView.as_view(template_name='maps.html'), name='maps'),
    path('data.geojson', GeoJSONLayerView.as_view(model=Record,
        properties=('coords'), geometry_field="coords"), name='data',),
    path('course/', include('course.urls')),
    
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
