numeroDeCarros, numeroDeVoltas = [int(x) for x in input().split(' ')]
listaDosTempos = []

for i in range(numeroDeCarros):
    tempoEmCadaVolta = [int(x) for x in input().split(' ')]
    listaDosTempos.append(sum(tempoEmCadaVolta))

for c in sorted(listaDosTempos)[:3]: print(listaDosTempos.index(c)+1)