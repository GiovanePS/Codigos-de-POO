repeticoes = int(input())
soma = 0

for c in range(repeticoes):
    soma += float(input())

print(f'{soma/repeticoes:.3f}')