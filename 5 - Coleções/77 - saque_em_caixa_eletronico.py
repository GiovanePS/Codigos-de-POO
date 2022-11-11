n_diferentesNotas = int(input())
v = {}
valores = {}
qntNotasSaque = 0
saida = []

for c in range(n_diferentesNotas):
    valorNota = float(input())
    qntNota = int(input())
    v[valorNota] = qntNota

for i in sorted(v, reverse = True):
    valores[i] = v[i]

valorSaque = float(input())

for k, v in valores.items():
    if valorSaque // k <= v:
        qntNotasSaque = valorSaque // k
        valorSaque -= qntNotasSaque * k
        saida.append(str(int(qntNotasSaque)))
    else:
        saida.append('0')
print(' '.join(reversed(saida)))