from django.urls import path
from .views import usd_graph

urlpatterns = [
    path("", usd_graph),
]
