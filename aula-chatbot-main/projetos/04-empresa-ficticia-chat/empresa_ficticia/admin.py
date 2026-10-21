"""Registra o modelo no Django Admin."""
from django.contrib import admin
from .models import RespostaChat

@admin.register(RespostaChat)
class RespostaChatAdmin(admin.ModelAdmin):
    list_display = ("pergunta", "resposta")
    search_fields = ("pergunta", "resposta")
