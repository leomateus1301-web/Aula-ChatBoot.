# 03 — Chat Integrado (Django)

Conversão do notebook `2 - Chat Integrado.ipynb` de Flask para Django. O layout original foi preservado: imagem de fundo, cabeçalho escuro translúcido, área institucional e chatbot flutuante com sugestões rápidas.

## Executar no Codespaces
Na raiz do repositório, execute:
```bash
cd projetos/03-chat-integrado
python -m pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```
Abra a porta 8000 em **Ports**. O primeiro acesso à página cadastra as respostas iniciais que ainda não existem.

## Documentação
- `docs/MATERIAL_DIDATICO.md`: explicação detalhada da arquitetura e dos arquivos.
- `docs/GUIA_LEITURA_DO_CODIGO.md`: roteiro para acompanhar a execução.

## Nota
A imagem de fundo e os ícones originais vêm de URLs externas; é necessária conexão à internet para carregá-los. O servidor Django usa SQLite local ao Codespace.
