casosDeTeste = int(input())
casoDeTeste = 0
arvores = list()
saida = ''

input()
while casoDeTeste < casosDeTeste:
    nomeDaEspecie = input()
    if nomeDaEspecie == '':
        casoDeTeste += 1
        arvores.sort()
        porcentagens = list()
        for x in sorted(set(arvores)):
            porcentagens.append(100*(arvores.count(x)/len(arvores)))
        for x in range(len(porcentagens)):
            saida += f'{sorted(set(arvores))[x]} {porcentagens[x]:.4f}\n'
        saida += '\n'
        arvores = list()
        porcentagens = list()
        continue
    arvores.append(nomeDaEspecie)

print(saida, end='')