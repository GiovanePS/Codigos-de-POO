salario = float(input())

if salario <= 720:
    valor_seguro = salario*7.65/100
elif salario <= 1200:
    valor_seguro = salario*9/100
elif salario <= 2400:
    valor_seguro = salario*11/100
else:
    valor_seguro = 2400*11/100

print(f'{valor_seguro:.2f}')