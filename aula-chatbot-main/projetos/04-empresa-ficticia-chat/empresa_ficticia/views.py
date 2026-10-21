"""Views do site institucional e da API do chatbot."""
import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from .models import RespostaChat

EXEMPLOS = [
    ("olá", "Olá! Como posso ajudar você hoje? 😊"),
    ("quais são os serviços oferecidos?", "Oferecemos desenvolvimento de software, consultoria em TI e soluções em nuvem."),
    ("vocês trabalham com inteligência artificial?", "Sim! Temos soluções personalizadas em IA para sua empresa."),
    ("como entro em contato?", "Você pode nos contatar pelo e-mail contato@empresa.com ou pelo telefone (11) 99999-9999."),
    ("ajuda", "Claro! Pergunte algo ou clique em um dos botões para começar."),
]

def index(request):
    for pergunta, resposta in EXEMPLOS:
        RespostaChat.objects.get_or_create(pergunta=pergunta, defaults={"resposta": resposta})
    return render(request, "empresa_ficticia/index.html")

@require_POST
def chat(request):
    try:
        payload = json.loads(request.body.decode("utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse({"resposta": "Não consegui ler sua mensagem. Tente novamente."}, status=400)

    pergunta = str(payload.get("pergunta", "")).strip().lower()
    if not pergunta:
        return JsonResponse({"resposta": "Digite uma pergunta para continuar."}, status=400)

    registro = RespostaChat.objects.filter(pergunta__iexact=pergunta).first()
    if registro:
        resposta = registro.resposta
    else:
        resposta = "Desculpe, não entendi sua pergunta. 🤔"
    return JsonResponse({"resposta": resposta})
