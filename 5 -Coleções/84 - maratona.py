postosDeAgua, distanciaIntermediariaMaxima = [int(x) for x in input().split(' ')]
posicaoDosPostosEmKM = [int(x) for x in input().split(' ')]

for i in range(1, len(posicaoDosPostosEmKM)):
    if posicaoDosPostosEmKM[i] < posicaoDosPostosEmKM[i-1]:
        print('N')
        break
    elif posicaoDosPostosEmKM[i] - posicaoDosPostosEmKM[i-1] > distanciaIntermediariaMaxima:
        print('N')
        break
    elif i < len(posicaoDosPostosEmKM)-1: continue
    print('S')