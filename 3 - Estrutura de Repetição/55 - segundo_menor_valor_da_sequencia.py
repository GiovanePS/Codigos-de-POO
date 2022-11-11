qntSequencia = int(input())

for _ in range(qntSequencia):
	valor = int(input())
	if _ == 0:
		menor = valor
		segundo_menor = valor
	elif valor < menor:
		segundo_menor = menor
		menor = valor
	elif valor < segundo_menor:
		segundo_menor = valor
		
print(segundo_menor)