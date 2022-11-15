while True:
    try:
        tamanhoLinha, tamanhoColuna = [int(x) for x in input().split()]
    except EOFError: break

    tabuleiro = [[int(i) for i in input().split()] for _ in range(tamanhoLinha)]

    soma = 0
    for x in range(tamanhoLinha):
        for y in range(tamanhoColuna):
            if tabuleiro[x][y] == 1: print(9, end='')
            else:
                if x != 0:
                    soma += tabuleiro[x-1][y]
                if x+1 != tamanhoLinha:
                    soma += tabuleiro[x+1][y]
                if y != 0:
                    soma += tabuleiro[x][y-1]
                if y+1 != tamanhoColuna:
                    soma += tabuleiro[x][y+1]
                print(soma, end='')
            soma = 0
        print()