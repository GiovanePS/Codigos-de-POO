quantidadeDeListas = int(input())
saida = ''

for x in range(quantidadeDeListas):
    produtosFinal = []
    produtos = [c for c in input().split(' ')]
    produtos.sort()
    for i in produtos:
        if i not in produtosFinal:
            produtosFinal.append(i)
    for i in produtosFinal:        
        saida += f'{i} '
    saida = saida.strip()
    saida += '\n'

print(saida)