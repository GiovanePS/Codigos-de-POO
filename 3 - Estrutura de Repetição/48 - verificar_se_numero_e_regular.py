n = int(input())
teste = False

while n > 1:
    if n % 2 == 0:
        teste = True
        n /= 2
    elif n % 3 == 0:
        teste = True
        n /= 3
    elif n % 5 == 0:
        teste = True
        n /= 5
    else:
        teste = False
        break

print(teste)