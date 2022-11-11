from math import inf

teste = 1
while True:
    n_Aeroportos, n_Voos = [int(x) for x in input().split(' ')]
    if n_Aeroportos == 0 and n_Voos == 0: break
    qntAeroportos = list(range(1, n_Aeroportos+1))

    listagem = []
    for _ in range(n_Voos):
        aeroportoOrigem, aeroportoDestino = [int(x) for x in input().split(' ')]
        listagem.append(aeroportoOrigem)
        listagem.append(aeroportoDestino)

    dicio = {}
    maior = -inf
    for x in set(listagem):
        dicio[x] = listagem.count(x)
        if listagem.count(x) > maior:
            maior = listagem.count(x)

    txt = ''
    for k, v in dicio.items():
        if v == maior:
            txt += f'{k} '

    print(f'Teste {teste}\n{txt.strip()}')
    teste += 1
    print()