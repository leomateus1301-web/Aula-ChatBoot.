"""Modelo de dados: perguntas e respostas do chatbot."""
from django.db import models


class RespostaChat(models.Model):
    pergunta = models.CharField(max_length=250, unique=True)
    resposta = models.TextField()

    class Meta:
        ordering = ["pergunta"]
        verbose_name = "Pergunta e resposta"
        verbose_name_plural = "Perguntas e respostas"

    def __str__(self):
        return self.pergunta
