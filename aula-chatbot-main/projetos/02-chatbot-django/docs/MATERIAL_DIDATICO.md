# Material didático — Chatbot em Django

## Identidade visual preservada

A conversão mantém o desenho do chatbot original em Flask: fundo cinza-claro, cartão central branco com sombra e cantos arredondados, cabeçalho azul com o título “Chatbot”, tela inicial branca com botão verde “Iniciar Conversa”, balões de conversa, botões rápidos azuis e campo de entrada arredondado. A mudança de Flask para Django altera a organização do backend, não a aparência esperada da página.

O CSS fica em `static/chatbot/style.css`. O template carrega esse arquivo usando `{% load static %}` e `{% static 'chatbot/style.css' %}`. Se a página aparecer sem formatação, confira o caminho, a raiz do projeto e se o servidor está rodando no diretório que contém `manage.py`; depois faça recarga forçada com `Ctrl+Shift+R`.

## 1. Objetivo da atividade

Este projeto transforma um chatbot simples em uma aplicação web com **Django**, HTML, CSS, JavaScript e banco de dados SQLite. A atividade ajuda a entender como a interface do navegador conversa com o servidor e como as perguntas e respostas podem ser armazenadas.

> **Importante:** este é um chatbot baseado em regras e correspondência de texto. Ele não utiliza um modelo de inteligência artificial generativa. Quando não reconhece uma pergunta, devolve uma resposta padrão.

## 2. Arquitetura em uma visão

1. O aluno abre a página inicial no navegador.
2. O Django entrega o template `templates/chatbot/index.html`.
3. O JavaScript captura a pergunta digitada ou o botão clicado.
4. `fetch()` envia a pergunta em JSON para `/chat/`.
5. A rota `/chat/` direciona a requisição para a função `chat()` em `chatbot/views.py`. O uso da barra final é importante: o template obtém o endereço por `{% url 'chat' %}` para evitar divergência entre o caminho do frontend e a rota Django.
6. A view normaliza a pergunta e consulta o modelo `RespostaChat`.
7. O Django devolve um JSON com a resposta.
8. O JavaScript mostra a resposta na conversa.

```text
Navegador
  ├── HTML: estrutura da página
  ├── CSS: aparência
  └── JavaScript: eventos e requisições fetch()
                 │ POST /chat/ (JSON + CSRF)
                 ▼
Django: urls.py → views.py → models.py/ORM → SQLite
                 │ JSON com a resposta
                 ▼
Navegador: JavaScript atualiza a conversa
```

## 3. Estrutura de pastas e arquivos

| Arquivo/pasta | Responsabilidade |
|---|---|
| `manage.py` | Ferramenta de linha de comando para executar tarefas do Django. |
| `requirements.txt` | Lista as bibliotecas Python necessárias; neste projeto, Django. |
| `chatbot_project/settings.py` | Configura o projeto: aplicações, banco, templates, idioma e arquivos estáticos. |
| `chatbot_project/urls.py` | Define as rotas principais do projeto. |
| `chatbot_project/wsgi.py` | Ponto de integração WSGI para servidores de aplicação compatíveis. |
| `chatbot/models.py` | Define o modelo `RespostaChat`, que representa perguntas e respostas no banco. |
| `chatbot/views.py` | Implementa a página inicial e a API que processa perguntas. |
| `chatbot/urls.py` | Mapeia os caminhos da aplicação para as views. |
| `chatbot/admin.py` | Configura o modelo para edição pela interface administrativa. |
| `chatbot/migrations/` | Guarda instruções versionadas para criar ou alterar tabelas. |
| `templates/chatbot/index.html` | Estrutura HTML e JavaScript da interface. |
| `static/chatbot/style.css` | Estilos visuais da interface. |
| `db.sqlite3` | Banco de dados criado ao executar as migrações e usar a aplicação. |

## 4. Conceitos fundamentais do Django

### Projeto e aplicação

- **Projeto** (`chatbot_project`): configurações gerais e rotas principais do site.
- **Aplicação** (`chatbot`): funcionalidade específica do chatbot, com modelos, views e rotas próprias.

Um projeto Django pode conter várias aplicações reutilizáveis.

### Requisição e resposta HTTP

O navegador faz uma requisição HTTP ao servidor. O Django processa a requisição e retorna uma resposta. A página inicial usa uma resposta HTML; o endpoint `/chat/` retorna JSON.

### URL e view

Uma rota associa um caminho a uma função. Por exemplo, `/chat/` é associado à função `chat()`. A rota não contém a lógica de resposta: ela direciona a requisição à view.

## 5. Explicação dos arquivos principais

### `requirements.txt`

Contém `Django>=5.2,<6.0`.

- `Django` é o framework web usado no projeto.
- `>=5.2` pede uma versão igual ou superior a 5.2.
- `<6.0` limita a instalação à série 5.x.
- `python -m pip install -r requirements.txt` instrui o pip a instalar o que estiver listado nesse arquivo.

### `manage.py`

É o utilitário de linha de comando do Django. Ele permite executar comandos administrativos, por exemplo:

- `python manage.py check`: verifica problemas comuns de configuração.
- `python manage.py migrate`: aplica migrações ao banco.
- `python manage.py makemigrations`: cria arquivos de migração a partir de mudanças nos modelos.
- `python manage.py runserver 0.0.0.0:8000`: inicia o servidor de desenvolvimento na porta 8000, aceitando conexões encaminhadas pelo Codespaces.

`runserver` serve para desenvolvimento e ensino, não para publicar uma aplicação de produção na internet.

### `settings.py`

Principais configurações:

- `BASE_DIR`: caminho-base usado para localizar arquivos do projeto.
- `SECRET_KEY`: chave interna do Django. A chave deste exemplo é apenas para desenvolvimento; não deve ser usada em produção.
- `DEBUG = True`: mostra informações úteis durante o desenvolvimento. Em produção, deve ser desativado.
- `ALLOWED_HOSTS`: domínios aceitos pelo Django. O sufixo `.app.github.dev` permite os endereços encaminhados pelo Codespaces.
- `INSTALLED_APPS`: lista as aplicações habilitadas, incluindo `chatbot` e recursos internos do Django.
- `MIDDLEWARE`: componentes que processam requisições e respostas; entre eles está a proteção CSRF.
- `ROOT_URLCONF`: indica o arquivo com as rotas principais.
- `TEMPLATES`: informa como localizar e processar templates HTML.
- `DATABASES`: configura SQLite como banco de dados.
- `LANGUAGE_CODE` e `TIME_ZONE`: idioma e fuso horário.
- `STATIC_URL`: prefixo usado para servir arquivos estáticos durante o desenvolvimento.
- `DEFAULT_AUTO_FIELD`: tipo padrão de chave primária automática para modelos novos.

### `models.py`

O modelo `RespostaChat` descreve a tabela:

- `pergunta = models.CharField(max_length=250, unique=True)`: texto de até 250 caracteres e sem duplicatas.
- `resposta = models.TextField()`: texto da resposta.
- `class Meta`: define ordenação e nomes exibidos na interface administrativa.
- `__str__()`: define como cada registro será representado como texto.

O **ORM** (Object-Relational Mapping) permite consultar e alterar dados usando objetos Python em vez de escrever SQL manualmente. `RespostaChat.objects.filter(pergunta=pergunta)` consulta registros que correspondam à pergunta.

### Migrações e SQLite

O modelo Python descreve a estrutura desejada, mas a tabela precisa existir no banco. Os arquivos em `chatbot/migrations/` registram mudanças estruturais.

- `makemigrations`: gera a descrição de uma mudança no modelo.
- `migrate`: aplica essas mudanças ao banco SQLite.
- SQLite guarda os dados em um arquivo local chamado `db.sqlite3` dentro do ambiente de execução.

No Codespaces, o arquivo fica no ambiente remoto do aluno. Não é um banco compartilhado entre toda a turma.

### `views.py`

A lista `EXEMPLOS` contém perguntas e respostas iniciais.

A função `index(request)`:
1. percorre a lista de exemplos;
2. usa `get_or_create()` para inserir registros que ainda não existem;
3. renderiza `chatbot/index.html`.

A função `chat(request)`:
1. aceita apenas o método HTTP POST, devido ao decorador `@require_POST`;
2. lê o corpo da requisição e tenta interpretar JSON;
3. extrai a pergunta, remove espaços externos e converte o texto para minúsculas;
4. devolve erro HTTP 400 quando a mensagem é inválida ou vazia;
5. procura uma resposta cadastrada;
6. verifica regras simples para saudações e ajuda;
7. usa uma resposta padrão quando não reconhece a pergunta;
8. devolve o resultado com `JsonResponse`.

O código compara textos de maneira simples. Por exemplo, uma pergunta com palavras adicionais pode não corresponder exatamente a um registro existente. Isso pode ser uma melhoria futura.

### `urls.py`

Em `chatbot_project/urls.py`, `include('chatbot.urls')` encaminha as rotas da aplicação. Em `chatbot/urls.py`:

- `path('', views.index, name='index')` exibe a página inicial.
- `path('chat/', views.chat, name='chat')` recebe mensagens.

O nome `chat` pode ser usado no template por `{% url 'chat' %}`. Assim, o JavaScript obtém o caminho correto sem precisar escrever o endereço manualmente em vários lugares.

### `admin.py`

O decorador `@admin.register(RespostaChat)` registra o modelo no Django Admin. `list_display` escolhe as colunas da listagem e `search_fields` habilita pesquisa. Para entrar no Admin com autenticação, seria necessário criar um superusuário com `python manage.py createsuperuser`.

### `index.html`: HTML, template Django e JavaScript

- `<!DOCTYPE html>` indica HTML moderno.
- `lang="pt-BR"` informa o idioma da página.
- `<meta charset="UTF-8">` permite representar caracteres acentuados.
- A meta `viewport` ajuda a adaptar o layout a diferentes telas.
- `{% load static %}` habilita a tag de arquivos estáticos do Django.
- `{% static 'chatbot/style.css' %}` gera o endereço do CSS.
- `{% csrf_token %}` cria o token necessário para a proteção CSRF.
- `{% url 'chat' %}` resolve a URL da API pelo nome da rota.

JavaScript:
- `getElementById()` localiza elementos pelo identificador HTML.
- `addEventListener()` reage a cliques e ao envio do formulário.
- `event.preventDefault()` evita que o formulário recarregue a página.
- `fetch()` envia a pergunta ao servidor sem recarregar toda a página.
- `JSON.stringify()` transforma o objeto JavaScript em texto JSON.
- `await response.json()` lê a resposta JSON do Django.
- `textContent` insere o texto da mensagem sem interpretá-lo como HTML.
- `try/catch` trata falhas na comunicação.

O cabeçalho `X-CSRFToken` envia o token CSRF. A proteção CSRF ajuda a evitar que sites externos forcem o navegador autenticado a enviar requisições não desejadas. Neste exemplo não há login do usuário, mas o middleware CSRF do Django continua ativo.

### `style.css`

O CSS define cores, tamanhos, espaçamentos, alinhamento e aparência das mensagens e botões. Separar CSS do HTML facilita mudar o visual sem alterar a lógica do chatbot.

## 6. O que acontece quando o aluno envia uma pergunta?

Exemplo: o usuário digita `olá`.

1. O evento `submit` do formulário chama `enviarPergunta()`.
2. A função lê e normaliza o texto no navegador.
3. `fetch()` envia `{"pergunta":"olá"}` para `/chat/`.
4. O Django encontra a rota `chat/` e executa `views.chat`.
5. A view consulta `RespostaChat` no SQLite.
6. A resposta encontrada é convertida em JSON.
7. O JavaScript recebe o JSON e cria um elemento de mensagem na tela.

Se a pergunta não for encontrada, o chatbot usa as regras de saudação/ajuda ou retorna uma resposta padrão.

## 7. Como executar no GitHub Codespaces

Abra o terminal na raiz do projeto e execute:

```bash
python -m pip install -r requirements.txt
python manage.py check
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

Depois abra a aba **Ports**, localize a porta `8000` e selecione **Open in Browser**.

Se o professor fornecer um ZIP dentro de um repositório recém-criado, primeiro será necessário descompactar e copiar os arquivos do projeto para a raiz do repositório. O `manage.py` deve estar na pasta em que os comandos serão executados.

## 8. Exercícios práticos

1. **Alterar uma resposta:** modifique a resposta da pergunta `ajuda` em `EXEMPLOS`. Reinicie ou atualize a aplicação e observe o resultado. Atenção: `get_or_create()` não atualiza registros que já existem; se o registro já estiver no banco, altere-o pelo Admin ou exclua-o antes de testar.
2. **Adicionar uma pergunta:** inclua uma nova tupla em `EXEMPLOS`, por exemplo uma pergunta sobre horário de atendimento. Acesse a página para inserir o novo exemplo e teste a pergunta.
3. **Personalizar a interface:** altere o título do chatbot em `index.html` e uma cor em `style.css`.
4. **Investigar a requisição:** abra as ferramentas de desenvolvedor do navegador, guia Network/Rede, envie uma pergunta e observe a chamada `POST /chat/` e a resposta JSON.
5. **Analisar erros:** envie uma pergunta vazia e observe como o JavaScript evita enviá-la; investigue também a resposta padrão para perguntas desconhecidas.

## 9. Desafios de extensão

- Adicionar um campo de categoria ao modelo.
- Criar uma tela para cadastrar perguntas sem editar o código.
- Melhorar a comparação de perguntas para ignorar pontuação.
- Guardar um histórico de conversas em uma tabela separada.
- Criar testes automatizados para as regras do chatbot.
- Substituir o conjunto de regras por uma integração com um serviço de IA, estudando autenticação, custos e proteção de dados.

## 10. Glossário

- **Backend:** parte executada no servidor.
- **Frontend:** interface com a qual o usuário interage.
- **Framework:** conjunto organizado de ferramentas e convenções para desenvolver aplicações.
- **HTTP:** protocolo usado para comunicação entre navegador e servidor.
- **JSON:** formato textual para troca de dados estruturados.
- **ORM:** camada que permite interagir com o banco usando objetos e métodos Python.
- **Rota:** caminho que direciona uma requisição a uma função.
- **Template:** arquivo de apresentação que o Django processa para gerar HTML.
- **CSRF:** tipo de ataque que tenta induzir um navegador a enviar requisições não desejadas.
- **Migração:** instrução versionada para criar ou modificar a estrutura do banco de dados.


## 11. Diagnóstico visual e de comunicação

Se o site aparecer sem cores e sem layout, o navegador provavelmente não carregou o CSS. Confira:
1. `static/chatbot/style.css` está no repositório.
2. `index.html` tem `{% load static %}` e o `<link>` para `chatbot/style.css`.
3. O terminal está na pasta onde fica `manage.py`.
4. O servidor está em execução e a página foi aberta pela porta `8000` do Codespaces.
5. Tente `Ctrl+Shift+R` para ignorar o CSS em cache.

Se a página estiver estilizada, mas as perguntas exibirem “erro na comunicação”:
1. Confira se o terminal mostra o servidor Django ativo.
2. Confirme que o template usa `{% url 'chat' %}` e que `chatbot/urls.py` define `path('chat/', views.chat, name='chat')`.
3. Confira na aba Network/Rede se a requisição POST a `/chat/` retorna status 200.
4. O código envia o token CSRF pelo cabeçalho `X-CSRFToken`; não remova essa proteção para corrigir erros de rota.
