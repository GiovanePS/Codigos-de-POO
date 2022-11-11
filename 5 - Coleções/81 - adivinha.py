from math import inf
for c in range(int(input())):
    diferencaMaisProxima = inf
    qntAlunos, numeroSecreto = [int(x) for x in input().split(' ')]
    numeroDadoDosAlunos = [int(x) for x in input().split(' ')]
    for x in range(len(numeroDadoDosAlunos)):
        if numeroDadoDosAlunos[x] == numeroSecreto:
            msg = x+1
            break
        elif abs(numeroDadoDosAlunos[x] - numeroSecreto) < diferencaMaisProxima:
            diferencaMaisProxima = abs(numeroDadoDosAlunos[x] - numeroSecreto)
            msg = x+1
    print(msg)