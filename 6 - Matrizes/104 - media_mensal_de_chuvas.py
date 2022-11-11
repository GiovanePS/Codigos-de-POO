medias = list()
for x in range(12):
    chuvasNoMes = [float(i) for i in input().split()]
    mediaDeChuvasNoMes = sum(chuvasNoMes)/len(chuvasNoMes)
    medias.append(f'{mediaDeChuvasNoMes:.2f}')

print(*medias)