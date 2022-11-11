horas_trabalhadas = int(input())
hora_extra = int(input())
salario_bruto = (12.5*horas_trabalhadas)+((hora_extra*15.0))
reducao_ir = salario_bruto*(13/100)
reducao_inss = salario_bruto*(9/100)
salario_liquido = salario_bruto - reducao_ir - reducao_inss

print(f'- Salário Bruto : R$ {salario_bruto:.2f}')
print(f'- IR (13%) : R$ {reducao_ir:.2f}')
print(f'- INSS (9%) : R$ {reducao_inss:.2f}')
print(f'- Salário Líquido : R$ {salario_liquido:.2f}')