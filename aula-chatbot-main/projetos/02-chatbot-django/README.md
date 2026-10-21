# Chatbot em Django — identidade visual original preservada

Esta versão converte a lógica do chatbot Flask para Django e mantém a identidade visual do original:
cabeçalho azul, cartão central com sombra, tela inicial com botão verde **Iniciar Conversa**,
área de mensagens cinza, botões rápidos azuis e campo de texto arredondado.

## Arquivos
- `manage.py`: comandos de administração do Django.
- `requirements.txt`: dependências do projeto.
- `chatbot_project/settings.py`: configurações gerais e arquivos estáticos.
- `chatbot_project/urls.py`: rotas gerais.
- `chatbot/models.py`: modelo de perguntas e respostas.
- `chatbot/views.py`: página inicial e endpoint JSON `/chat/`.
- `chatbot/urls.py`: URLs da aplicação.
- `templates/chatbot/index.html`: HTML e JavaScript.
- `static/chatbot/style.css`: identidade visual original.
- `docs/MATERIAL_DIDATICO.md`: material didático detalhado.
- `docs/GUIA_LEITURA_DO_CODIGO.md`: guia de leitura do código.
- `.devcontainer/devcontainer.json`: preparação do ambiente Codespaces.

## Importante: como colocar os arquivos no GitHub
O ZIP contém uma pasta `chatbot_tratado_django`. Ao preparar o repositório, o conteúdo dessa pasta
precisa ficar diretamente na raiz do repositório (onde se vê `manage.py`), e não apenas o ZIP.

Se você já enviou o ZIP para um repositório vazio:
1. Abra um Codespace no repositório.
2. No terminal, execute `unzip Chatbot_Django_Identidade_Visual.zip` (ajuste ao nome real do ZIP).
3. Execute `cp -R chatbot_tratado_django/. .`.
4. Execute os comandos da seção seguinte.

## Executar
```bash
python -m pip install -r requirements.txt
python manage.py check
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```
Abra a aba **Ports**, encontre a porta `8000` e selecione **Open in Browser**.

## Se a página aparecer sem CSS
- Confirme que `static/chatbot/style.css` existe.
- Confirme que o HTML contém `{% load static %}` e a referência `{% static 'chatbot/style.css' %}`.
- Recarregue a página com `Ctrl+Shift+R`.
- Confirme que o servidor foi iniciado a partir da pasta que contém `manage.py`.
- No Codespaces, veja a aba Terminal e Ports; não use o link do navegador antigo após recriar o ambiente.

## Observação de segurança
É um projeto didático. `DEBUG=True` e a chave secreta de desenvolvimento não devem ser usadas em produção.
