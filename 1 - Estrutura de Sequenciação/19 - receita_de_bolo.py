xicara_farinha, ovos, colher_leite = [int(x) for x in input().split()]

xicara_farinha //= 2
ovos //= 3
colher_leite //= 5

max_bolos = min(xicara_farinha, ovos, colher_leite)

print(max_bolos)