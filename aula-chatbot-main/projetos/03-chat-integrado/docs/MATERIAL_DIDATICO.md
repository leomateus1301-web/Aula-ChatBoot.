# Material didático — Chat Integrado com Django

## 1. Objetivo
O projeto converte o notebook Flask para Django e mantém a proposta visual original: site de empresa de tecnologia, fundo com imagem, cabeçalho translúcido, texto institucional e chatbot flutuante no canto inferior direito.

## 2. Fluxo da aplicação
1. O navegador solicita `/`.
2. A rota `index` chama a view `index()` e renderiza o template.
3. Na primeira visita, a view cadastra as perguntas de exemplo ainda ausentes.
4. Ao clicar no ícone, o JavaScript abre o painel do chatbot.
5. Ao enviar uma pergunta, `fetch()` faz POST para `/chat/` com JSON e token CSRF.
6. A view `chat()` valida o JSON, consulta o ORM do Django e devolve JSON.
7. O JavaScript mostra a resposta no painel.

## 3. Estrutura dos arquivos
- `manage.py`: executa comandos do Django.
- `requirements.txt`: registra a dependência Django.
- `chat_integrado/models.py`: define a tabela lógica de perguntas e respostas.
- `chat_integrado/views.py`: inicializa exemplos e processa requisições.
- `chat_integrado/urls.py`: associa URLs às views.
- `chat_integrado/admin.py`: permite administrar perguntas e respostas no Admin.
- `chat_integrado/migrations/`: arquivos gerados por `makemigrations`.
- `chat_integrado_project/settings.py`: configura banco, aplicações, templates e arquivos estáticos.
- `templates/chat_integrado/index.html`: estrutura da página e JavaScript.
- `static/chat_integrado/style.css`: regras visuais extraídas do CSS original.
- `db_chat_integrado.sqlite3`: banco SQLite local, criado após `migrate`.

## 4. Modelo de dados e ORM
`Resposta` possui:
- `pergunta`: texto curto e único, usado para localizar a resposta.
- `resposta`: texto que o chatbot retorna.
- `__str__`: representação textual do registro.

O ORM (`Resposta.objects...`) traduz consultas Python para operações SQL. `get_or_create()` insere apenas quando a pergunta ainda não existe; não sobrescreve respostas já editadas.

## 5. Banco e migrações
O SQLite é configurado em `settings.py`. `makemigrations` cria a descrição versionada das mudanças no modelo; `migrate` cria/atualiza as tabelas no banco. Como cada aluno usa seu próprio Codespace, cada um tem seu próprio banco.

## 6. Rotas
- `/`: mostra o site.
- `/chat/`: recebe perguntas por POST e responde em JSON.
- `/admin/`: interface administrativa do Django, caso seja criado um superusuário.

## 7. HTML e template Django
- `{% load static %}` habilita a tag de arquivos estáticos.
- `{% static 'chat_integrado/style.css' %}` monta o caminho do CSS.
- `{% url 'chat' %}` obtém a URL da API a partir do nome da rota.
- `{% csrf_token %}` gera o token de proteção usado pelo JavaScript.
- `aria-label`, `aria-expanded` e `aria-hidden` ajudam tecnologias assistivas a entender o painel.

## 8. CSS e identidade visual
O CSS foi separado do HTML sem redesenhar a proposta original: fundo com imagem de componentes eletrônicos, cabeçalho preto translúcido, texto branco, painel branco flutuante, balões verdes/vermelhos suaves e botões de sugestões azuis. A regra `#chat-window` usa `display: none`; a classe `.aberto` ativa `display: flex` para abrir o painel. Isso corrige o conflito de duas declarações `display` presente no CSS original, preservando o comportamento pretendido.

## 9. JavaScript
- `addEventListener()` associa ações a cliques e ao envio do formulário.
- `fetch()` envia a pergunta ao Django sem recarregar a página.
- `JSON.stringify()` converte o objeto em JSON.
- `response.json()` interpreta a resposta.
- `textContent` exibe mensagens como texto, sem interpretá-las como HTML.
- `try/catch` mostra uma mensagem quando a chamada falha.
- `X-CSRFToken` envia o token esperado pelo middleware CSRF do Django.

## 10. Lógica do chatbot
A busca ignora diferença entre maiúsculas e minúsculas, mas exige que o texto seja igual à pergunta cadastrada, depois de remover espaços externos. Não é IA generativa nem compreensão semântica; perguntas diferentes recebem uma resposta padrão.

## 11. Testes sugeridos
- Abrir e fechar o painel no ícone flutuante.
- Testar os quatro botões de pergunta rápida.
- Enviar uma pergunta digitada e pressionar Enter.
- Testar uma pergunta desconhecida.
- Na aba Network/Rede do navegador, conferir POST `/chat/` e resposta JSON.
- Conferir no terminal que `GET /static/chat_integrado/style.css` retorna status 200.

## 12. Exercícios
1. Acrescente uma pergunta e resposta em `EXEMPLOS`.
2. Personalize o texto do cabeçalho sem alterar o CSS.
3. Adicione um botão de pergunta rápida.
4. Ajuste a largura do painel para telas pequenas.
5. Explique a diferença entre uma rota, uma view e um modelo.
