nLinhas, nColunas = [int(x) for x in input().split()]

matriz = [[int(x) for x in input().split()] for _ in range(nLinhas)]

#Linhas
maiorSoma = 0
for x in matriz:
    if sum(x) > maiorSoma: maiorSoma = sum(x)

#Colunas
for y in range(nColunas):
    soma = 0
    for x in range(nLinhas):
        soma += matriz[x][y]
    if soma > maiorSoma: maiorSoma = soma

print(maiorSoma)