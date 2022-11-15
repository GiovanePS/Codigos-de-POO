while True:
    try: tamanhoLinha, tamanhoColuna = [int(i) for i in input().split()]
    except EOFError: break

    analogimon = jogador = None
    for x in range(tamanhoLinha):
        posicao = [int(x) for x in input().split()]
        if analogimon != None and jogador != None: continue
        for y in range(tamanhoColuna):
            if posicao[y] == 1: jogador = (x, y)
            if posicao[y] == 2: analogimon = (x, y)

    passos = abs(analogimon[0] - jogador[0]) + abs(analogimon[1] - jogador[1])
    print(passos)