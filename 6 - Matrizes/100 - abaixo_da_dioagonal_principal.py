operacao = input()

soma = 0
for x in range(12):
    for y in range(12):
        valor = float(input())
        if y < x: soma += valor

print(f'{soma:.1f}' if operacao == 'S' else f'{soma/66:.1f}')