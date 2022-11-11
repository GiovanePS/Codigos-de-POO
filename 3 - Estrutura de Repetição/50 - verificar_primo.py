numero = int(input())
primo = True

if numero != 1 and numero != 0:
	for c in range(2, int(numero**(1/2) + 1)):
		if numero % c == 0:
			if c != numero:
				primo = False
				break
else:
	primo = False

print(primo)