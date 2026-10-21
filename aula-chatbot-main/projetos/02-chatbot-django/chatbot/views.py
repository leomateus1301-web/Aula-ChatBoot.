"""
VIEWS: recebem requisições HTTP, executam a lógica da aplicação
e devolvem uma resposta ao navegador.
"""
import json  # Converte texto JSON recebido em um dicionário Python.
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from .models import RespostaChat  # Importa o modelo definido em models.py.


# Conjunto inicial de perguntas e respostas para demonstrar o chatbot.
# Os dados serão cadastrados no banco quando a página inicial for acessada.
EXEMPLOS = [
    ("olá", "Olá! Como posso ajudar você hoje? 😊"),
    ("quais são os serviços oferecidos?", "Oferecemos desenvolvimento de software, consultoria em TI e soluções em nuvem."),
    ("vocês trabalham com inteligência artificial?", "Sim! Temos soluções personalizadas em IA para sua empresa."),
    ("como entro em contato?", "Você pode nos contatar pelo e-mail contato@empresa.com ou pelo telefone (11) 99999-9999."),
    ("ajuda", "Claro! Pergunte algo ou clique em um dos botões para começar."),
]


def index(request):
    """
    Exibe a página principal do chatbot.

    request contém informações da requisição feita pelo navegador.
    get_or_create cria cada exemplo somente se ele ainda não existir,
    evitando duplicações ao atualizar a página.
    """
    for pergunta, resposta in EXEMPLOS:
        RespostaChat.objects.get_or_create(
            pergunta=pergunta,
            defaults={'resposta': resposta}
        )

    # render localiza o template HTML, processa as tags Django e o devolve.
    return render(request, 'chatbot/index.html')


@require_POST
def chat(request):
    """
    API do chatbot. Aceita somente requisições HTTP POST.
    Espera um corpo JSON semelhante a: {"pergunta": "olá"}
    e devolve JSON semelhante a: {"resposta": "Olá! ..."}.
    """
    try:
        # request.body contém os bytes enviados pelo navegador.
        # decode transforma bytes em texto; json.loads transforma JSON em dict.
        data = json.loads(request.body.decode('utf-8'))
    except (json.JSONDecodeError, UnicodeDecodeError):
        # HTTP 400 indica que a requisição veio com conteúdo inválido.
        return JsonResponse(
            {'resposta': 'Não consegui ler a mensagem. Tente novamente.'},
            status=400
        )

    # get evita erro se a chave não existir; str garante texto;
    # strip remove espaços nas pontas e lower padroniza para minúsculas.
    pergunta = str(data.get('pergunta', '')).strip().lower()

    if not pergunta:
        return JsonResponse(
            {'resposta': 'Digite uma pergunta para continuar.'},
            status=400
        )

    # ORM do Django: consulta a tabela sem escrever SQL diretamente.
    registro = RespostaChat.objects.filter(pergunta=pergunta).first()

    if registro:
        resposta = registro.resposta
    # Respostas simples para saudações mesmo que não estejam cadastradas.
    elif any(saudacao in pergunta for saudacao in ['olá', 'ola', 'oi', 'oii']):
        resposta = 'Olá! Que bom falar com você. Clique nos botões ou digite sua dúvida.'
    elif 'ajuda' in pergunta:
        resposta = 'Claro! Use os botões abaixo ou digite sua pergunta.'
    else:
        # Este chatbot usa correspondência simples de texto; não é IA generativa.
        resposta = 'Desculpe, não entendi sua pergunta. Por favor, tente uma das opções abaixo.'

    # JsonResponse converte o dicionário Python em JSON para o JavaScript.
    return JsonResponse({'resposta': resposta})
