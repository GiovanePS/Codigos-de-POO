valoresRomanos = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
numeroRomano = input().upper()

decimal = 0

for i in range(len(numeroRomano)-1):
    dr = numeroRomano[i]
    dr_seguinte = numeroRomano[i+1]
    if valoresRomanos[dr] >= valoresRomanos[dr_seguinte]:
        decimal += valoresRomanos[dr]
    else:
        decimal -= valoresRomanos[dr]

decimal += valoresRomanos[numeroRomano[-1]]

print(decimal)