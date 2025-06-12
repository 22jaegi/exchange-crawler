from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("usd/", include("usd.urls")),  # usd 앱 연결
]
