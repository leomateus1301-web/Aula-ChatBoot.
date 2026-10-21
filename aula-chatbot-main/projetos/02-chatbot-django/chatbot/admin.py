"""Configura como o modelo aparece na interface administrativa do Django."""
from django.contrib import admin
from .models import RespostaChat


@admin.register(RespostaChat)
class RespostaChatAdmin(admin.ModelAdmin):
    # Colunas que aparecem na listagem de registros do Admin.
    list_display = ('pergunta', 'resposta')
    # Campos pesquisáveis na barra de busca do Admin.
    search_fields = ('pergunta', 'resposta')
