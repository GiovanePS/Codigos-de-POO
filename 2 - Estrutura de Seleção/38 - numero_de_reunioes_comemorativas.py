aniversario1 = int(input())
aniversario2 = int(input())
aniversario3 = int(input())

if aniversario1 == aniversario2 == aniversario3:
	print(1)
elif aniversario1 == aniversario2 or aniversario2 == aniversario3 or aniversario1 == aniversario3:
	print(2)
else:
	print(3)