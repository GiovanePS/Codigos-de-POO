dimensaoDaMatriz = int(input())
p, q, r, s, x, y = [int(x) for x in input().split()]
LinhaASerConsultada, ColunaASerConsultada = [int(x) for x in input().split()]

ALinha = [(p*LinhaASerConsultada + q*j)%x for j in range(1, dimensaoDaMatriz+1)]
BColuna = [(r*i + s*ColunaASerConsultada)%y for i in range(1, dimensaoDaMatriz+1)]

ValorBuscado = sum(ALinha[i]*BColuna[i] for i in range(dimensaoDaMatriz))
print(ValorBuscado)