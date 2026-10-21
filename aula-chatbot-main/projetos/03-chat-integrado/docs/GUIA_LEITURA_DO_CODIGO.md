# Guia de leitura do código — Chat Integrado

Leia nesta ordem:
1. `chat_integrado/models.py`: estrutura dos dados.
2. `chat_integrado/views.py`: dados iniciais e API.
3. `chat_integrado/urls.py` e `chat_integrado_project/urls.py`: caminhos.
4. `templates/chat_integrado/index.html`: HTML, template tags e JavaScript.
5. `static/chat_integrado/style.css`: identidade visual.
6. `chat_integrado_project/settings.py`: configuração global.

## Rastreie uma pergunta
Localize `enviarPergunta()` no HTML, depois `path("chat/", ...)` na rota e `def chat(request)` na view. Compare a chave JSON `pergunta` enviada com a chave `resposta` devolvida.

## Pontos para explicar em aula
- Por que `fetch()` não recarrega a página?
- Por que Django precisa do token CSRF?
- Qual é a diferença entre `CharField` e `TextField`?
- O que o ORM faz quando chamamos `Resposta.objects.filter(...)`?
- Por que `get_or_create()` evita duplicar as perguntas?
- O que muda visualmente quando a classe `aberto` é adicionada ao painel?
