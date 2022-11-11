consumoMensal = int(input())
valorFinal = 0

if consumoMensal >= 30:
	valorFinal += 0.09556*30
	if consumoMensal >= 100:
		valorFinal += 0.16698*(100-30)
		if consumoMensal >= 200:
			valorFinal += 0.25052*(200-100) + (consumoMensal-200)*0.27836
		else:
			valorFinal += 0.25052*(consumoMensal-100)
	else:
		valorFinal += 0.16698*(consumoMensal-30)
else:
	valorFinal = 0.09556*consumoMensal
	
print(f'{valorFinal:.2f}')