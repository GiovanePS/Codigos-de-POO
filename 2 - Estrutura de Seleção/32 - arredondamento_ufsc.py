nota = float(input())

if nota - int(nota) < 0.25 or nota - int(nota) >= 0.75:
	print(round(nota))
elif 0.25 <= nota - int(nota) < 0.75:
	print(int(nota) + 0.5)