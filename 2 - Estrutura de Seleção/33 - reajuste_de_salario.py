salarioAtual = float(input())
salarioMinimo = float(input())

if salarioAtual < salarioMinimo * 1.5:
	reajuste = salarioMinimo*1.5
elif salarioAtual <= 3*salarioMinimo:
	reajuste = salarioAtual + salarioAtual * 20/100
elif salarioAtual <= 5*salarioMinimo:
	reajuste = salarioAtual + salarioAtual * 15/100
else:
	reajuste = salarioAtual + salarioAtual * 10/100

if reajuste > 20*salarioMinimo:
	print(f'{salarioMinimo*20:.2f}')
else:
	print(reajuste)