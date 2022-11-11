from math import inf
praias = int(input())
distancia_praiaMaisDistante = -inf
praiasEntre20e30km = distanciaMedia = 0


for c in range(praias):
	nome_praia, distancia = input().split(';')
	distancia = int(distancia)
	if distancia > distancia_praiaMaisDistante:
		distancia_praiaMaisDistante = distancia
		nome_praiaMaisDistante = nome_praia
	
	if 15 <= distancia <= 20:
		praiasEntre20e30km += 1
		
	distanciaMedia += distancia
	
distanciaMedia /= praias

print(f'{nome_praiaMaisDistante};{praiasEntre20e30km};{distanciaMedia:.1f}')