auxiliar = input().strip().split()
numeroDeJogadores, partidas = int(auxiliar[0]), int(auxiliar[1])

jogadoresQueSempreMarcaram = 0
for x in range(numeroDeJogadores):
    marcou = True
    golsDoJogador = [int(x) for x in input().split(' ')]
    for y in golsDoJogador:
        if y <= 0:
            marcou = False
            break
    if marcou == True: jogadoresQueSempreMarcaram += 1

print(jogadoresQueSempreMarcaram)