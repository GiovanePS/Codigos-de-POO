n = int(input())
valores = [float(input()) for x in range(n)]

media = sum(valores) / n
soma = sum((x - media) ** 2 for x in valores)

desvioPadrao = (soma/(n-1))**(1/2)
print(desvioPadrao)