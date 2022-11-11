def findLeft(posicaoDoBalao, valoresNaLinha):
    c = 0
    while valoresNaLinha[posicaoDoBalao-c] == 0:
        c += 1
        if posicaoDoBalao-c < 0: return [0, 0]
    return [valoresNaLinha[posicaoDoBalao-c], posicaoDoBalao-c+1]

def findRight(posicaoDoBalao, valoresNaLinha):
    c = 0
    while valoresNaLinha[posicaoDoBalao+c] == 0:
        c += 1
        if posicaoDoBalao+c >= len(valoresNaLinha): return [0, posicaoDoBalao+c]
    return [valoresNaLinha[posicaoDoBalao+c], posicaoDoBalao+c+1]

while True:
    linhas, colunas, posicaoDoBalao = [int(x) for x in input().split()]
    if linhas == colunas == posicaoDoBalao == 0: break
    balaoEstourou = False
    estouroX, estouroY = 0, 0
    for x in range(linhas):
        valoresNaLinha = [int(x) for x in input().split()]
        if balaoEstourou: continue
        ventiladorEsquerda, ventiladorDireita = findLeft(posicaoDoBalao - 1, valoresNaLinha), findRight(posicaoDoBalao - 1, valoresNaLinha)
        ventiladorEsquerda, indiceDaPosicaoEsquerda = ventiladorEsquerda[0], ventiladorEsquerda[1]
        ventiladorDireita, indiceDaPosicaoDireita = ventiladorDireita[0], ventiladorDireita[1]
        if ventiladorEsquerda > ventiladorDireita:
            posicaoDoBalao += ventiladorEsquerda - ventiladorDireita
            if posicaoDoBalao > indiceDaPosicaoDireita: posicaoDoBalao = indiceDaPosicaoDireita
        else:
            posicaoDoBalao -= ventiladorDireita - ventiladorEsquerda
            if posicaoDoBalao < indiceDaPosicaoEsquerda: posicaoDoBalao = indiceDaPosicaoEsquerda
        if posicaoDoBalao < 0 or posicaoDoBalao > len(valoresNaLinha) or valoresNaLinha[posicaoDoBalao-1] != 0:
            balaoEstourou = True
            estouroX, estouroY = x+1, posicaoDoBalao

    print(f'OUT {posicaoDoBalao}' if not balaoEstourou else f'BOOM {estouroX} {estouroY}')