while True:
    n_jogadoresAtacantes, n_jogadoresDefensivos = [int(x) for x in input().split(' ')]
    if n_jogadoresAtacantes == 0 and n_jogadoresDefensivos == 0: break
    impedido = False
    distanciaDosAtacantes = [int(x) for x in input().split(' ')]
    distanciaDosDefensores = [int(x) for x in input().split(' ')]
    distanciaDosAtacantes.sort(reverse=True)
    distanciaDosDefensores.sort(reverse=True)

    if len(distanciaDosDefensores) >= 2: y = -2
    else: y = -1

    for x in range(len(distanciaDosAtacantes)):
        if distanciaDosAtacantes[x] < distanciaDosDefensores[y]:
            impedido = True
            break

    print('Y' if impedido else 'N')