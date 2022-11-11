valor_veiculo =  float(input())
classe_desconto = input()
procedencia = input()
idade_do_segurado = int(input())

if procedencia == 'nacional':
    premio = valor_veiculo*1/10
elif procedencia == 'estrangeira':
    premio = valor_veiculo*15/100

valor = premio

if classe_desconto == 'A':
    premio -= premio * 30/100
elif classe_desconto == 'B':
    premio -= premio * 20/100
elif classe_desconto == 'C':
    premio -= premio * 10/100
elif classe_desconto == 'D':
    premio -= premio * 5/100

if idade_do_segurado > 24:
    premio -= valor * 10/100

print(premio)