competidores, folhas_compradas, folha_por_competidor = [int(x) for x in input().split()]

if folhas_compradas // competidores >= folha_por_competidor:
    print('S')
else:
    print('N')