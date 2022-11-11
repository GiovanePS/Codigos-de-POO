while True:
    n_pessoasQueUtilizaramAEscada = int(input())
    if n_pessoasQueUtilizaramAEscada == 0: break
    tempos = [int(x) for x in input().split(' ')]
    tempoFinal = len(tempos)*10
    for x in range(n_pessoasQueUtilizaramAEscada-1, 0, -1):
        if tempos[x] in range(tempos[x-1], tempos[x-1]+10):
            tempoFinal -= 10 - (tempos[x] - tempos[x-1])
    print(tempoFinal)