qntSaltadores = int(input())

for c in range(qntSaltadores):
	nota1, nota2, nota3, nome = [x for x in input().split(' ')]
	nota1, nota2, nota3 = float(nota1), float(nota2), float(nota3)
	if c == 0:
		notaMaior = max(nota1, nota2, nota3)
		nomeMelhor = nome
	elif max(nota1, nota2, nota3) > notaMaior:
		notaMaior = max(nota1, nota2, nota3)
		nomeMelhor = nome
	
print(nomeMelhor)