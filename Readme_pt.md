# Chatbot em Python

Este repositório contém um chatbot simples em Python que responde a mensagens predefinidas. O chatbot usa um dicionário de regras, onde cada palavra-chave está associada a uma resposta. Ele processa a entrada do usuário, procura por palavras-chave correspondentes e retorna a resposta adequada. Caso não haja correspondência, ele solicita que o usuário repita a mensagem.

## Funcionalidades

- Responde a diversos cumprimentos e perguntas.
- Lida com mensagens como "Olá", "Bom dia" e "Boa noite".
- Oferece respostas predefinidas para perguntas sobre sua identidade, programação e outros tópicos.
- Conta piadas e compartilha curiosidades.
- O usuário pode sair do chat digitando "sair".

## Como Funciona

O chatbot ouve a entrada do usuário, compara com um conjunto de regras predefinidas e responde de acordo. Caso não haja correspondência, ele pedirá para o usuário repetir a mensagem.


## Requisitos

- Python 3.x

Não são necessárias bibliotecas adicionais para rodar este chatbot.

## Como Usar

1. Clone ou baixe este repositório.
2. Abra o script em qualquer editor de Python ou IDE.
3. Execute o script.
4. Interaja com o chatbot digitando suas mensagens.
5. Digite "sair" para encerrar a conversa.

## Explicação do Código

- **Dicionário `regras`**: Contém pares de palavra-chave e resposta. Cada palavra-chave está mapeada para uma resposta específica.
- **Função `chatbot_resp`**: Recebe uma mensagem de entrada do usuário, converte para minúsculas e verifica se há correspondência com as palavras-chave no dicionário `regras`. Se houver correspondência, retorna a resposta correspondente.
- **Loop Principal**: O loop principal aguarda a entrada do usuário e continua até que o usuário digite "sair".

## Personalizando o Chatbot

Você pode modificar as respostas atualizando o dicionário `regras`. Adicione novas palavras-chave e respostas para tornar o chatbot mais interativo ou personalizado de acordo com suas necessidades.


