frase = input().lower()
frase = frase.replace(' ', '')

letraAnterior = ''
letras = {}
qntDaLetra = 0
for c in sorted(frase):
    if c == letraAnterior:
        qntDaLetra += 1
        letras[c] = qntDaLetra
    else:
        letras[c] = 1
        letraAnterior = c
        qntDaLetra = 0

print(list(letras.keys())[list(letras.values()).index(max(letras.values()))])