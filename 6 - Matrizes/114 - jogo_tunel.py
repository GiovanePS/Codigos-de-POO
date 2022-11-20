while True:
    try: linhasMatriz, colunasMatriz = [int(x) for x in input().split()]
    except EOFError: break
    matriz = [[int(x) if x.isnumeric() else x for x in input().split()] for _ in range(linhasMatriz)]
    for linha in range(len(matriz)):
        if 'X' in matriz[linha]: x, y = linha, matriz[linha].index('X')

    direcao = None
    txt = ''
    while True:
        if direcao != None: txt += 'F '
        matriz[x][y] = 1
        achouLadrilho = False
        if x != 0:
            if matriz[x-1][y] == 0:
                x -= 1
                achouLadrilho = True
                posicaoLadrilho = 'cima'
        
        if not achouLadrilho and x+1 < linhasMatriz:
            if matriz[x+1][y] == 0:
                x += 1
                achouLadrilho = True
                posicaoLadrilho = 'baixo'

        if not achouLadrilho and y != 0:
            if matriz[x][y-1] == 0:
                y -= 1
                achouLadrilho = True
                posicaoLadrilho = 'esquerda'

        if not achouLadrilho and y+1 < colunasMatriz:
            if matriz[x][y+1] == 0:
                y += 1
                achouLadrilho = True
                posicaoLadrilho = 'direita'

        if not achouLadrilho:
            txt += 'E'
            break

        if direcao == None:
            if posicaoLadrilho == 'cima': direcao = 'N'
            elif posicaoLadrilho == 'baixo': direcao = 'S'
            elif posicaoLadrilho == 'esquerda': direcao = 'O'
            elif posicaoLadrilho == 'direita': direcao = 'L'

        if direcao == 'S': #sul
            if posicaoLadrilho == 'esquerda':
                txt += 'R '
                direcao = 'O'
            elif posicaoLadrilho == 'direita':
                txt += 'L '
                direcao = 'L'
        elif direcao == 'N': #norte
            if posicaoLadrilho == 'esquerda':
                txt += 'L '
                direcao = 'O'
            elif posicaoLadrilho == 'direita':
                txt += 'R '
                direcao = 'L'
        elif direcao == 'L': #leste
            if posicaoLadrilho == 'cima':
                txt += 'L '
                direcao = 'N'
            elif posicaoLadrilho == 'baixo':
                txt += 'R '
                direcao = 'S'
        elif direcao == 'O': #oeste
            if posicaoLadrilho == 'cima':
                txt += 'R '
                direcao = 'N'
            elif posicaoLadrilho == 'baixo':
                txt += 'L '
                direcao = 'S'
            
    print(txt)