# Guia de leitura do código — Empresa Fictícia com Chat

Ordem sugerida:
1. `empresa_ficticia/models.py`: campos armazenados.
2. `empresa_ficticia/views.py`: exemplos iniciais e lógica da API.
3. `empresa_ficticia/urls.py`: caminhos da aplicação.
4. `templates/empresa_ficticia/index.html`: estrutura, eventos e requisição fetch.
5. `static/empresa_ficticia/style.css`: identidade visual.
6. `empresa_ficticia_project/settings.py`: banco, templates e estáticos.

Para rastrear uma mensagem, procure `sendMessage()` no JavaScript, siga `chatUrl` até a rota `chat/` e depois encontre `def chat(request)` em `views.py`.

Perguntas para discussão:
- Por que o JavaScript envia JSON?
- O que o decorador `require_POST` protege?
- Por que o token CSRF é enviado?
- Como `get_or_create()` evita duplicatas?
- O que acontece quando a pergunta não existe no banco?
