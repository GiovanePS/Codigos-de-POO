dimensaoDaMatriz = int(input())
valorEhConstante = True

matriz = [[int(y) for y in input().split()] for x in range(dimensaoDaMatriz)]
for x in matriz: print(x)
valorConstante = sum(matriz[0])

#Verificar Linha
for x in matriz:
    if sum(x) != valorConstante:
        valorEhConstante = False
        break

#Verificar coluna
if valorEhConstante:
    for y in range(len(matriz)):
        soma = 0
        for x in range(len(matriz)): soma += matriz[x][y]
        if soma != valorConstante:
            valorEhConstante = False
            break

#Verificar diagonal principal
if valorEhConstante:
    soma = 0
    for i in range(len(matriz)): soma += matriz[i][i]
    if soma != valorConstante: valorEhConstante = False

#Verificar diagonal secundária
if valorEhConstante:
    soma, x, y = 0, 0, len(matriz)-1
    for i in range(len(matriz)):
        soma += matriz[x][y]
        x += 1
        y -= 1
    if soma != valorConstante: valorEhConstante = False

print(valorEhConstante)