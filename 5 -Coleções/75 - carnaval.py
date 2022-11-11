notas = [float(x) for x in input().split(' ')]
notas.remove(max(notas))
notas.remove(min(notas))
print(f'{sum(notas):.1f}')