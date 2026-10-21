"""Views do chatbot integrado à página de uma empresa de tecnologia."""
import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from .models import Resposta

EXEMPLOS = [
    ("Olá", "Olá! Como posso te ajudar hoje?"),
    ("Qual é o horário de funcionamento?", "Estamos abertos das 10h às 22h todos os dias."),
    ("Vocês fazem entrega?", "Sim, fazemos entrega em toda a cidade."),
    ("Qual o telefone de contato?", "Nosso telefone é (11) 1234-5678."),
    ("Qual o endereço?", "Estamos localizados na Av. Central, 123, São Paulo - SP."),
]

def index(request):
    # Cria somente exemplos ausentes, sem apagar alterações já feitas no banco.
    for pergunta, resposta in EXEMPLOS:
        Resposta.objects.get_or_create(pergunta=pergunta, defaults={"resposta": resposta})
    return render(request, "chat_integrado/index.html")

@require_POST
def chat(request):
    # A API espera JSON: {"pergunta": "..."}.
    try:
        payload = json.loads(request.body.decode("utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse({"resposta": "Não consegui ler a pergunta. Tente novamente."}, status=400)

    pergunta = str(payload.get("pergunta", "")).strip()
    if not pergunta:
        return JsonResponse({"resposta": "Digite uma pergunta."}, status=400)

    # A busca ignora diferenças entre maiúsculas e minúsculas, preservando o texto original no banco.
    registro = Resposta.objects.filter(pergunta__iexact=pergunta).first()
    resposta = registro.resposta if registro else "Desculpe, não entendi sua pergunta. Tente outra."
    return JsonResponse({"resposta": resposta})
