bandejas = int(input())
coposQuebrados = 0

for _ in range(bandejas):
    latas, copos = [int(x) for x in input().split(' ')]
    if latas > copos:
        coposQuebrados += copos

print(coposQuebrados)