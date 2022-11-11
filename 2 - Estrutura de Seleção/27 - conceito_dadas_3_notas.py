nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
media = (nota1 + nota2 + nota3)/3

if media < 6:
    print('Insuficiente')
elif media <= 7.5:
    print('Satisfatório')
elif media <= 9:
    print('Bom')
else:
    print('Ótimo')