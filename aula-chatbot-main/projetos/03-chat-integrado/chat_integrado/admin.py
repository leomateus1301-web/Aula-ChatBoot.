"""Registra o modelo no Django Admin."""
from django.contrib import admin
from .models import Resposta

@admin.register(Resposta)
class RespostaAdmin(admin.ModelAdmin):
    list_display = ("pergunta", "resposta")
    search_fields = ("pergunta", "resposta")
