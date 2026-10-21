"""Rotas principais do projeto: ponto de entrada para as rotas das aplicações."""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),  # Interface administrativa em /admin/.
    path('', include('chatbot.urls')),  # Encaminha a raiz para chatbot/urls.py.
]
