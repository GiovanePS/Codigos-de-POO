area_para_pintar = int(input())
galoes = round((area_para_pintar/18)/3.6)
galoes = max(1, galoes)

print(f'- área de cobertura: {area_para_pintar}')
print(f'- número de galões: {galoes}')
print(f'- valor a ser pago: R$ {galoes*25:.2f}')