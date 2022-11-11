listagem = []
while True:
    n_perguntasRealizadas, qnt_ParaPerguntaSerFrequente = [int(x) for x in input().split(' ')]
    if n_perguntasRealizadas == 0 and qnt_ParaPerguntaSerFrequente == 0: break
    pergunta = [int(x) for x in input().split(' ')]
    
    perguntaFrequente = 0
    for x in set(pergunta):
        if pergunta.count(x) >= qnt_ParaPerguntaSerFrequente:
            perguntaFrequente += 1
                
    print(perguntaFrequente)