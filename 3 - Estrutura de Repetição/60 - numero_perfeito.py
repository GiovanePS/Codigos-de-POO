casosDeTeste = int(input())

for _ in range(casosDeTeste):
	numero = int(input())
	soma = 0
	for c in range(1, numero):
		if numero % c == 0:
			soma += c
			
	if soma == numero: print(f'{numero} eh perfeito')
	else: print(f'{numero} nao eh perfeito')