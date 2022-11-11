x = int(input())
y = int(input())
primos = 0

if x == 1: x += 1

for i in range(x, y+1):
	verificarPrimo = True
	divisor = 0
	for j in range(1, i+1):
		if i % j == 0:
			divisor += 1
			
		if divisor > 2:
			verificarPrimo = False
			break
		
	if verificarPrimo:
		primos += 1
		
print(primos)