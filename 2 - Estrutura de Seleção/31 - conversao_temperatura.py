escala_origem = input()
valor_temperatura = float(input())
escala_destino = input()

if escala_origem == 'c':
	temp_to_c = valor_temperatura
elif escala_origem == 'f':
	temp_to_c = (valor_temperatura - 32) * 5/9
elif escala_origem == 'k':
	temp_to_c = valor_temperatura - 273.15
elif escala_origem == 'r':
	temp_to_c = (valor_temperatura - 491.67) * 5/9
	
if escala_destino == 'c':
	print(temp_to_c)
elif escala_destino == 'f':
	print(temp_to_c * 9/5 + 32)
elif escala_destino == 'k':
	print(temp_to_c + 273.15)
elif escala_destino == 'r':
	print(temp_to_c * 9/5 + 491.67)