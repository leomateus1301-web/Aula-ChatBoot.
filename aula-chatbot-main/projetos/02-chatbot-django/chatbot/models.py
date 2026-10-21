"""
MODELOS: definem como os dados serão organizados no banco de dados.

Neste projeto, cada registro representa uma pergunta e a resposta
que o chatbot deve devolver quando reconhecer essa pergunta.
"""
from django.db import models


class RespostaChat(models.Model):
    # CharField guarda texto curto. max_length limita a pergunta a 250 caracteres.
    # unique=True impede duas linhas com a mesma pergunta.
    pergunta = models.CharField(max_length=250, unique=True)

    # TextField guarda texto de tamanho maior, adequado para a resposta.
    resposta = models.TextField()

    class Meta:
        # Ordena os registros alfabeticamente quando forem consultados.
        ordering = ['pergunta']
        # Nomes exibidos no Django Admin, em singular e plural.
        verbose_name = 'Resposta do chatbot'
        verbose_name_plural = 'Respostas do chatbot'

    def __str__(self):
        # Define a representação textual do registro no Admin e em depuração.
        return self.pergunta
