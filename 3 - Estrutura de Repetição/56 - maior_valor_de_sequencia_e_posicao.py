qntSequencia = int(input())

for c in range(1, qntSequencia+1):
	valor = int(input())
	if c == 1:
		maior = valor
		posicao = c
	elif valor > maior:
		maior = valor
		posicao = c
		
print(maior, posicao)