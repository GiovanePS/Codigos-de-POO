componente1 = input().lower()
componente2 = input().lower()
fraseCriptografada = input().lower()
fraseDescriptografada = ''

for y in fraseCriptografada:
    letra = False
    for x in zip(componente2, componente1):
        if y == x[0]:
            fraseDescriptografada += x[1]
            letra = True
            break
    if letra == False: fraseDescriptografada += y

print(fraseDescriptografada)