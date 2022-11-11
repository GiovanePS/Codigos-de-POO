primeiro_valor = int(input())
ultimo_valor = int(input())

if ultimo_valor > primeiro_valor:
    print(ultimo_valor - primeiro_valor + 1)
else:
    print(primeiro_valor - ultimo_valor + 1)