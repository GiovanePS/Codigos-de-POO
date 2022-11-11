n = int(input())
valores = [float(input()) for _ in range(n)]

produto = 1
for c in valores:
    produto *= c

print((produto)**(1/n))