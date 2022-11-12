txt = ''
while True:
    tamanhoDaMatriz = int(input())
    if tamanhoDaMatriz == 0: break

    matriz = [[2**(i+x) for i in range(tamanhoDaMatriz)] for x in range(tamanhoDaMatriz)]

    t = len(str(matriz[-1][-1]))
    for x in range(tamanhoDaMatriz):
        for i in matriz[x]:
            txt += f'{i:>{t}} '
        txt = txt.rstrip()
        txt += '\n'
    txt += '\n'

print(txt.rstrip())
#print() caso envio for no beecrowd