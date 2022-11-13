while True:
    try:
        tamanhoDaMatriz = int(input())
    except EOFError:
        break
    for x in range(tamanhoDaMatriz):
        for y in range(tamanhoDaMatriz):
            if x == (tamanhoDaMatriz-1)/2 and y == (tamanhoDaMatriz-1)/2: print(4, end='')
            elif tamanhoDaMatriz//3 <= x < tamanhoDaMatriz-tamanhoDaMatriz//3 and tamanhoDaMatriz//3 <= y < tamanhoDaMatriz-tamanhoDaMatriz//3: print(1, end='')
            elif x+1 + y+1 == tamanhoDaMatriz+1: print(3, end='')
            elif x == y: print(2, end='')
            else: print(0, end='')
        print()
    print()