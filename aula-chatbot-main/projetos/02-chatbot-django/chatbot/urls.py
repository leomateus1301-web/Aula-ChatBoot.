"""Rotas da aplicação chatbot: relacionam caminhos a funções de views."""
from django.urls import path
from . import views

urlpatterns = [
    # URL raiz do site -> função index, que mostra a página.
    path('', views.index, name='index'),
    # URL /chat/ -> função chat, que recebe as perguntas por POST.
    # O name='chat' permite referenciar esta rota pelo nome no template.
    path('chat/', views.chat, name='chat'),
]
