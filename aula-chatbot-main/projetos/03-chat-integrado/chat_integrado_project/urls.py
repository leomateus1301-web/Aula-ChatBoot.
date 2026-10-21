"""Rotas gerais do projeto."""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("chat_integrado.urls")),
]
