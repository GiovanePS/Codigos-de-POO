conector1 = [int(x) for x in input().split(' ')]
conector2 = [int(x) for x in input().split(' ')]

for i in range(5):
    if conector1[i] == conector2[i]:
        print('N')
        break
    elif i < 4: continue
    print('Y')