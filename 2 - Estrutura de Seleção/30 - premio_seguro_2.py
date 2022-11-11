valor_veiculo = float(input())
sexo = input()
idade = int(input())

valor_premio = valor_veiculo*10/100

if sexo == 'M':
    if 25 <= idade <= 33:
        valor_premio -= valor_premio*10/100
    elif idade > 33:
        valor_premio -= valor_premio*20/100
elif sexo == 'F':
    if idade <= 24:
        valor_premio -= valor_premio*5/100
    elif idade <= 33:
        valor_premio -= valor_premio*20/100
    else:
        valor_premio -= valor_premio*35/100

print(valor_premio)