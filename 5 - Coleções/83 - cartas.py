cartas = [int(x) for x in input().split(' ')]

if sorted(cartas) == cartas: print('C')
elif sorted(cartas, reverse = True) == cartas: print('D')
else: print('N')