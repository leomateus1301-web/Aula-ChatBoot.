# Guia de leitura do código

Este guia complementa os comentários presentes nos arquivos `.py`, no HTML e no CSS.

## Ordem recomendada para estudar
1. `chatbot/models.py`: compreenda primeiro como uma resposta é representada.
2. `chatbot/views.py`: siga a lógica que carrega exemplos e processa perguntas.
3. `chatbot/urls.py` e `chatbot_project/urls.py`: descubra como as URLs chegam às funções.
4. `templates/chatbot/index.html`: observe os elementos da interface e o JavaScript.
5. `static/chatbot/style.css`: veja como a interface ganha aparência visual.
6. `chatbot_project/settings.py`: revise as configurações que conectam as partes.
7. `chatbot/admin.py` e `chatbot/migrations/`: entenda a administração e a estrutura do banco.

## Como investigar uma pergunta
Use a busca do editor para localizar `enviarPergunta` no HTML e `def chat` em `views.py`.
Compare:
- o nome da URL usada pelo `fetch`;
- o método HTTP enviado;
- a chave JSON `pergunta`;
- a consulta ao modelo;
- a chave JSON `resposta` devolvida ao navegador.

## Atenção ao `get_or_create`
A função `index()` insere os exemplos que ainda não existem, mas não atualiza uma resposta já cadastrada. Isso é intencional para evitar sobrescrever alterações feitas no banco. Para alterar respostas existentes, use o Django Admin ou atualize os dados de forma explícita.

## Limites da demonstração
- O chatbot não aprende com a conversa e não gera respostas por IA.
- O banco SQLite é local ao Codespace de cada aluno.
- O servidor `runserver` é para desenvolvimento, não produção.
- A chave secreta e `DEBUG=True` são configurações didáticas; não devem ser copiadas para uma publicação real.


## Como a identidade visual é mantida
Abra `static/chatbot/style.css` e observe os seletores `#chat-container`, `#chat-header`, `#chat-log`, `#quick-questions`, `#input-area` e `#start-chat`. Eles reproduzem a organização visual do chatbot original em Flask. O arquivo HTML não deve depender de estilos embutidos: ele carrega o CSS por meio da tag estática do Django.
