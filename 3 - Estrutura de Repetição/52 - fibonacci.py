nTermo = int(input())

a = 0
b = 1
contador = 0
while True:
	a, b = a + b, a
	contador += 1
	if contador == nTermo: break
	
print(a)