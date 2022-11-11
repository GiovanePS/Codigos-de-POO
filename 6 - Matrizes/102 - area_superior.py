operacao = input()

soma = 0
for x in range(12):
    for y in range(12):
        valor = float(input())
        if y > x and x + y < 11: soma += valor

print(f'{soma:.1f}' if operacao == 'S' else f'{soma/30:.1f}')