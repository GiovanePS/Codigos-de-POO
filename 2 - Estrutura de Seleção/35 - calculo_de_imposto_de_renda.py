salarioBruto = float(input())
dependentes = int(input())

if salarioBruto <= 720:
	inss = salarioBruto*7.65/100
elif salarioBruto <= 1200:
	inss = salarioBruto*9/100
elif salarioBruto <= 2400:
	inss = salarioBruto*11/100
else:
	inss = 2400*11/100

if salarioBruto <= 1372.81:
	aliquota = 0
	deducao = 0
elif 1372.81 < salarioBruto <= 2743.25:
	aliquota = 15/100
	deducao = 205.92
else:
	aliquota = 27.5/100
	deducao = 548.82

impostoDeRenda = (salarioBruto - 137.99*dependentes - inss)*aliquota - deducao

if impostoDeRenda < 0:
	print(0.0)
else:
	print(f'{impostoDeRenda:.2f}')