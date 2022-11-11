x = 1
while True:
	n = 1
	for c in range(1, x+1):
		n *= c
		
	if n > x**10:
		print(x)
		break
	
	x += 1