instancias = int(input())

for jogo in range(instancias):
    solucao = True
    sudoku = [[int(y) for y in input().split()] for x in range(9)]
    
    #Verificar Linha
    for x in sudoku:
        if len(set(x)) != 9:
            solucao = False
            break

    #Verificar Coluna
    if solucao:
        for y in range(len(sudoku)):
            coluna = []
            for x in range(len(sudoku)):
                coluna.append(sudoku[x][y])
            if len(set(coluna)) != 9:
                solucao = False
                break

    #Verificar 3x3
    if solucao:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                matriz3x3 = []
                for x in range(3):
                    for y in range(3): matriz3x3.append(sudoku[i+x][j+y])
                if len(set(matriz3x3)) != 9:
                    solucao = False
                    break
            if solucao == False: break

    print(f'Instancia {jogo+1}')
    print('SIM' if solucao else 'NAO')