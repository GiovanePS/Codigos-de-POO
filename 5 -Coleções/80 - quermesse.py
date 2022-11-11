teste = 0
while True:
    teste += 1
    numeroParticipantes = int(input())
    if numeroParticipantes == 0: break
    ordemEntrada = [int(x) for x in input().split()]
    for i in range(len(ordemEntrada)):
        if ordemEntrada[i] == i+1:
            print(f'Teste {teste}\n{ordemEntrada[i]}', end='\n\n')