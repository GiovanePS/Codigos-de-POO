def mostrar_proporcoes():
    for madeira, qnt in sorted(contagem.items()):
            proporcao = qnt * 100 / num_madeiras
            print(madeira, f"{proporcao:.4f}")

casosDeTeste = int(input())
input()

while True:
    try:
        contagem = dict()
        num_madeiras = 0

        while True:
            madeira = input()
            if madeira == '': break
            if madeira in contagem:
                contagem[madeira] += 1
            else:
                contagem[madeira] = 1
            num_madeiras += 1
        mostrar_proporcoes()
        print()
    except EOFError:
        mostrar_proporcoes()
        break