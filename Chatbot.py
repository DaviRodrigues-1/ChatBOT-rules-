regras = {
    "olá": "Oi, como posso ajudar?",
    "oi": "Oi, como posso ajudar?",
    "oii": "Oi, como posso ajudar?",
    "bom dia": "Oi, como posso ajudar?",
    "boa tarde": "Boa tarde! Como posso ajudar?",
    "boa noite": "Boa noite! Como posso ajudar?",
    "ajuda": "Claro! Me diga como posso ajudar.",
    "horas": "Eu não sei as horas, mas posso responder outras dúvidas.",
    "nome": "Eu sou um chatbot criado por você!",
    "tchau": "Até logo! Se precisar de mais ajuda, estarei aqui.",
    "obrigado": "De nada! Estou aqui para ajudar.",
    "como você está?": "Eu sou um chatbot, então sempre estou bem! Como posso ajudar você?",
    "qual o seu nome?": "Eu sou um chatbot criado por você!",
    "o que você faz?": "Eu estou aqui para responder suas perguntas e ajudar no que for possível.",
    "me conte uma piada": "Por que o livro de matemática se suicidou? Ele tinha muitos problemas.",
    "qual é a capital do Brasil?": "A capital do Brasil é Brasília.",
    "quantos anos você tem?": "Eu sou um chatbot, então não tenho idade!",
    "de onde você é?": "Eu fui criado para ajudar você aqui.",
    "qual é a sua cor favorita?": "Eu sou um chatbot, então não tenho uma cor favorita.",
    "você gosta de música?": "Eu não posso ouvir música, mas sei que muitas pessoas gostam!",
    "qual é o sentido da vida?": "Essa é uma grande pergunta! Muitas pessoas acreditam que é encontrar felicidade e propósito.",
    "você pode me ajudar com programação?": "Claro! Me diga qual é a sua dúvida sobre programação.",
    "me recomende um filme": "Eu recomendo assistir 'O Poderoso Chefão'! É um clássico.",
    "me recomende um livro": "Eu recomendo 'Dom Quixote' de Miguel de Cervantes. É um clássico da literatura.",
    "você sabe jogar xadrez?": "Eu conheço as regras do xadrez, mas não posso jogar. Posso te ajudar a aprender as regras!",
    "qual é o seu animal favorito?": "Eu sou um chatbot, então não tenho um animal favorito.",
    "me conte uma curiosidade": "Você sabia que o coração de um camarão está em sua cabeça?",
    "qual é a sua comida favorita?": "Eu sou um chatbot, então não como, mas sei que pizza é uma escolha popular!",


}

def chatbot_resp(mensagem):
    mensagem = mensagem.lower()
    
    for palavra, resposta in regras.items():
        if palavra in mensagem:
            return resposta
        
    return "Desculpe, não entendi. Pode repetir?"

print("Olá! Eu sou um chatbot. Digite 'sair' para encerrar.")

while True: 
    entrada = input("Você: ")
    if entrada.lower() == "sair":
        print("Até logo")
        break
    resposta = chatbot_resp(entrada)
    print(f"Chatbot: {resposta}")
 