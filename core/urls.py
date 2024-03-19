from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("campaign_api.urls", namespace="campaign_api")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path('activate/<uid>/<token>/', RedirectView.as_view(url='http://localhost:5173/activate/%(uid)s/%(token)s')),
]
