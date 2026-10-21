# 04 — Empresa Fictícia com Chat (Django)

Conversão do notebook `3 - Empresa Ficticia com Chat.ipynb` de Flask para Django. Preserva a página institucional com cabeçalho e rodapé azuis, texto de apresentação, botão flutuante e painel de chat.

## Executar no Codespaces
```bash
cd projetos/04-empresa-ficticia-chat
python -m pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```
Abra a porta 8000 na aba **Ports**.

## Documentação
- `docs/MATERIAL_DIDATICO.md`
- `docs/GUIA_LEITURA_DO_CODIGO.md`

## Observação
O chatbot usa correspondência textual simples e SQLite. Não é um sistema de IA generativa.
