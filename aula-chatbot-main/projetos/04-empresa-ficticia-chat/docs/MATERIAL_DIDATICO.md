# Material didático — Empresa Fictícia com Chat em Django

## 1. Objetivo
Aplicação web de uma empresa fictícia com chatbot flutuante. A conversão usa Django no backend e preserva a identidade visual do notebook: cabeçalho e rodapé azuis, conteúdo central, botão circular flutuante e janela de conversa branca.

## 2. Fluxo de execução
1. O navegador abre `/`.
2. A view `index()` cadastra os exemplos ausentes e renderiza o template.
3. O CSS define o layout e o estado fechado do painel.
4. O JavaScript abre/fecha o painel e envia perguntas com `fetch()`.
5. A rota `/chat/` direciona a requisição POST para `views.chat`.
6. A view consulta o modelo pelo ORM e retorna JSON.
7. A interface exibe a resposta sem recarregar a página.

## 3. Arquivos
- `manage.py`: interface de linha de comando do Django.
- `requirements.txt`: dependência Django.
- `empresa_ficticia/models.py`: modelo de pergunta e resposta.
- `empresa_ficticia/views.py`: inserção de exemplos, renderização e endpoint.
- `empresa_ficticia/urls.py`: rotas da aplicação.
- `empresa_ficticia/admin.py`: registro do modelo no Admin.
- `empresa_ficticia_project/settings.py`: configuração do projeto, banco e arquivos estáticos.
- `empresa_ficticia_project/urls.py`: rotas principais.
- `templates/empresa_ficticia/index.html`: estrutura da página e JavaScript.
- `static/empresa_ficticia/style.css`: CSS separado do HTML.
- `docs/`: documentação de estudo.

## 4. Modelo e banco SQLite
`RespostaChat` contém `pergunta` (texto curto único) e `resposta` (texto longo). O Django ORM permite consultar registros com `RespostaChat.objects.filter(...)`. O SQLite é criado/atualizado por `migrate`; cada Codespace tem seu banco próprio.

## 5. Migrações
`python manage.py makemigrations` cria o arquivo que descreve como construir a tabela a partir do modelo. `python manage.py migrate` aplica a migração. Sempre que um modelo for alterado, verifique se será necessária nova migração.

## 6. Rotas e API
- `/`: renderiza a página institucional.
- `/chat/`: recebe JSON por POST e devolve `{"resposta": "..."}`.
- `/admin/`: painel administrativo, disponível após criar superusuário.
A barra final na URL `/chat/` é importante porque a URL é gerada no template com `{% url 'chat' %}`.

## 7. Template e arquivos estáticos
`{% load static %}` habilita a tag `static`. `{% static 'empresa_ficticia/style.css' %}` aponta para o CSS. `STATICFILES_DIRS` em `settings.py` informa a pasta `static` da raiz do projeto ao Django. Se o CSS não carregar, rode `python manage.py findstatic empresa_ficticia/style.css` e confira se o GET do CSS retorna HTTP 200.

## 8. HTML, CSS e JavaScript
- O HTML estrutura cabeçalho, conteúdo, rodapé e painel do chatbot.
- O CSS preserva cores, espaçamento, sombras, botão flutuante e balões.
- `classList.toggle()` ativa/desativa a classe `aberto`.
- `addEventListener()` associa ações aos botões e formulário.
- `fetch()` envia a pergunta ao backend sem recarregar a página.
- `JSON.stringify()` serializa a pergunta.
- `response.json()` interpreta a resposta.
- `textContent` insere texto sem interpretá-lo como HTML.
- O cabeçalho `X-CSRFToken` envia o token de proteção CSRF.

## 9. Lógica do chatbot
As perguntas iniciais são inseridas com `get_or_create()`, evitando duplicatas. A busca ignora maiúsculas/minúsculas, mas precisa corresponder ao texto cadastrado. Uma pergunta desconhecida recebe uma resposta padrão; não há IA generativa.

## 10. Exercícios
1. Adicione uma pergunta sobre horário de atendimento.
2. Modifique o texto de boas-vindas.
3. Crie um botão rápido que envie uma pergunta nova.
4. Altere a cor do cabeçalho em `style.css`.
5. Inspecione a requisição POST `/chat/` na guia Network/Rede do navegador.
6. Explique a relação entre URL, view, modelo e banco de dados.
