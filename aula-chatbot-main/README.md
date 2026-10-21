# Aula Chatbot — Coleção de projetos didáticos

Repositório do professor para compartilhar exemplos de chatbots e aplicações web usados nas aulas de programação, Python, Cloud, IoT e Indústria 4.0.

## Projetos disponíveis

| Pasta | Projeto | Tecnologia | Situação |
|---|---|---|---|
| [`projetos/02-chatbot-django/`](projetos/02-chatbot-django/) | Chatbot com perguntas rápidas e interface visual preservada | Django, HTML, CSS, JavaScript e SQLite | Em preparação |

Novos projetos serão incluídos em pastas próprias, sem misturar seus arquivos ou dependências.

## Como estudar um projeto

1. Abra a pasta do projeto desejado.
2. Leia o `README.md` dentro da pasta.
3. Consulte `docs/MATERIAL_DIDATICO.md` e `docs/GUIA_LEITURA_DO_CODIGO.md`.
4. Siga as instruções específicas para executar o projeto no GitHub Codespaces.

## Estrutura do repositório

```text
aula-chatbot/
├── README.md
├── .gitignore
├── .devcontainer/
├── docs/
├── projetos/
│   └── 02-chatbot-django/
│       ├── manage.py
│       ├── requirements.txt
│       ├── chatbot/
│       ├── chatbot_project/
│       ├── templates/
│       ├── static/
│       └── docs/
└── recursos/
```

## Ambiente de desenvolvimento

O Codespaces será criado na raiz do repositório. Como cada chatbot pode ter dependências próprias, abra a pasta do projeto e siga o respectivo README para instalar dependências e executar o servidor.

Para o chatbot Django:

```bash
cd projetos/02-chatbot-django
python -m pip install -r requirements.txt
python manage.py check
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

Em seguida, abra a aba **Ports**, localize a porta `8000` e selecione **Open in Browser**.

## Boas práticas
- Não versionar bancos SQLite gerados durante a execução, arquivos de ambiente, tokens ou senhas.
- Manter cada projeto isolado em sua própria pasta.
- Atualizar este índice sempre que um novo chatbot for incluído.
