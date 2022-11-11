numeroDeBolasDaPrimeiraFileira = int(input())
bolasDaFileiraAtual = [int(x) for x in input().split(' ')]

for x in range(numeroDeBolasDaPrimeiraFileira-1):
    bolasDaProximaFileira = []
    for y in range(len(bolasDaFileiraAtual)-1):
        if bolasDaFileiraAtual[y] == bolasDaFileiraAtual[y+1]:
            bolasDaProximaFileira.append(1)
        else:
            bolasDaProximaFileira.append(-1)
    bolasDaFileiraAtual = bolasDaProximaFileira[:]

for x in bolasDaFileiraAtual: print('branca' if x == -1 else 'preta')