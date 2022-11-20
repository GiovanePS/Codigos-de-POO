linhasSalao, colunasSalao = [int(x) for x in input().split()]
x, y = [int(i)-1 for i in input().split()]

matriz = [[int(i) for i in input().split()] for _ in range(linhasSalao)]

while True:
    AchouLadrilho = False
    matriz[x][y] = 0
    if x != 0:
        if matriz[x-1][y] == 1:
            x -= 1
            AchouLadrilho = True
            continue
    
    if x+1 < linhasSalao:
        if matriz[x+1][y] == 1:
            x += 1
            AchouLadrilho = True
            continue

    if y != 0:
        if matriz[x][y-1] == 1:
            y -= 1
            AchouLadrilho = True
            continue

    if y+1 < colunasSalao:
        if matriz[x][y+1] == 1:
            y += 1
            AchouLadrilho = True
            continue

    if AchouLadrilho == False: break

print(x+1, y+1)