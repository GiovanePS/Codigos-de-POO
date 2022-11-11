capital = float(input())
meses = int(input())
taxa = float(input())/100

montante = capital*(1+taxa)**meses

print(f'{montante:.2f}')