paredes = int(input())

for p in range(paredes):
    linhasMatriz, colunasMatriz, linhaDoSoco, colunaDoSoco = [int(x) for x in input().split()]
    
    matriz = [[int(i) for i in input().split()] for _ in range(linhasMatriz)]
    for x in range(linhasMatriz):
        for y in range(colunasMatriz):
            hipotenusa = int(((linhaDoSoco-1 - x)**2 + (colunaDoSoco-1 - y)**2)**(1/2))
            if hipotenusa > 9: hipotenusa = 9
            matriz[x][y] += 10 - hipotenusa

    print(f'Parede {p+1}:')
    for x in matriz: print(*x)