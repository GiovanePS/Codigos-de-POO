conceito1 = input()
conceito2 = input()
conceito3 = input()
conceito4 = input()

if conceito1 == 'A':
	conceito1 = 4
elif conceito1 == 'B':
	conceito1 = 3
elif conceito1 == 'C':
	conceito1 = 2
elif conceito1 == 'E':
	conceito1 = 0
	
if conceito2 == 'A':
	conceito2 = 4
elif conceito2 == 'B':
	conceito2 = 3
elif conceito2 == 'C':
	conceito2 = 2
elif conceito2 == 'E':
	conceito2 = 0
	
if conceito3 == 'A':
	conceito3 = 4
elif conceito3 == 'B':
	conceito3 = 3
elif conceito3 == 'C':
	conceito3 = 2
elif conceito3 == 'E':
	conceito3 = 0
	
if conceito4 == 'A':
	conceito4 = 4
elif conceito4 == 'B':
	conceito4 = 3
elif conceito4 == 'C':
	conceito4 = 2
elif conceito4 == 'E':
	conceito4 = 0

indiceAproveitamento = (conceito1 + conceito2 + conceito3 + conceito4) / 4

if indiceAproveitamento >= 3 and conceito1 > 0 and conceito2 > 0 and conceito3 > 0 and conceito4 > 0:
	print('true')
else:
	print('false')