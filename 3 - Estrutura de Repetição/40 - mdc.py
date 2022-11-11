numero1 = int(input())
numero2 = int(input())

while numero2 > 0:
    resto = numero1 % numero2
    numero1 = numero2
    numero2 = resto

print(numero1)