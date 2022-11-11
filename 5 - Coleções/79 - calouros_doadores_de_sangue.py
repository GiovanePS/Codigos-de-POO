numero_Calouros = int(input())
nome_Calouros = [input() for _ in range(numero_Calouros)]
numero_Total = int(input())
nome_Total = [input() for _ in range(numero_Total)]

calourosDoadores = 0
for nome in nome_Total:
    if nome in nome_Calouros: calourosDoadores += 1

print(f'{calourosDoadores/numero_Calouros:.5f}')