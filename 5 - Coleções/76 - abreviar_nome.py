nomeCompleto = input().split(' ')
nome = nomeCompleto[0]
sobrenome = nomeCompleto[-1]

for c in range(len(nomeCompleto)):
    if len(nomeCompleto[c]) > 3 and c != nomeCompleto.index(nome) and c != nomeCompleto.index(sobrenome):
        nomeCompleto[c] = nomeCompleto[c][0]+'.'

print(' '.join(nomeCompleto))