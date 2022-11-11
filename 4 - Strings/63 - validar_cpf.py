cpf = input().replace('.', '').replace('-', '')

if len(cpf) == 11 and cpf[0]*11 != cpf:
    digito_cpf = 0
    soma = 0
    for c in range(10, 1, -1):
        soma += int(cpf[digito_cpf]) * c
        digito_cpf += 1
    if soma % 11 <= 1: digito_verificador_1 = 0
    else: digito_verificador_1 = 11 - soma % 11

    if digito_verificador_1 == int(cpf[9]):
        digito_cpf = 0
        soma = 0
        for c in range(11, 1, -1):
            soma += int(cpf[digito_cpf]) * c
            digito_cpf += 1
        if soma % 11 <= 1: digito_verificador_2 = 0
        else: digito_verificador_2 = 11 - soma % 11

        digitos_verificadores = int(str(digito_verificador_1) + str(digito_verificador_2))
        print(digitos_verificadores == int(cpf[9:11]))
    else:
        print(False)
else: print(False)