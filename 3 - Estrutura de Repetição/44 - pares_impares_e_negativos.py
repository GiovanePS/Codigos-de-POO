pares = impares = negativos = positivos = 0

for _ in range(5):
    valor = int(input())
    if valor % 2 == 0:
        pares += 1
    else:
        impares += 1

    if valor < 0:
        negativos += 1
    elif valor > 0:
        positivos += 1

print(f'{pares} valor(es) par(es)\n{impares} valor(es) impar(es)\n{positivos} valor(es) positivo(s)\n{negativos} valor(es) negativo(s)')