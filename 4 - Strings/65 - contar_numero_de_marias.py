numeroDeEntradas = int(input())
qnt_Maria = 0

for _ in range(numeroDeEntradas):
    nome = input()
    for c in nome.split(' '):
        if c == 'Maria': qnt_Maria += 1

print(qnt_Maria)