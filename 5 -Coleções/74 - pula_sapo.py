alturaDoPulo, nCanos = [int(x) for x in input().split(' ')]
alturaOrdenadaDosCanos = [int(x) for x in input().split(' ')]
vitoria = True

for i in range(1, len(alturaOrdenadaDosCanos)):
    proxCano = alturaOrdenadaDosCanos[i]
    if abs(alturaOrdenadaDosCanos[i-1] - proxCano) > alturaDoPulo:
        vitoria = False
        break

print('YOU WIN' if vitoria == True else 'GAME OVER')