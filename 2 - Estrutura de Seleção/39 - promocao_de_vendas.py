gastoTotal = float(input())

gastoDescontado = gastoTotal - (gastoTotal*20/100)

if gastoTotal >= 500:
	gastoDescontado -= gastoTotal*10/100
	
if gastoTotal > 1000:
	gastoTotal -= 1000
	gastoDescontado -= (gastoTotal*15/100)
	
print(f'{gastoDescontado:.2f}')