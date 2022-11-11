while True:
	retangulos = varetasParaFormarRetangulos = 0
	variaveisVaretas = int(input())
	if variaveisVaretas == 0: break
	for _ in range(variaveisVaretas):
		comprimento, qntVaretas = [int(x) for x in input().split(' ')]
		if qntVaretas >= 4:
			retangulos += qntVaretas // 4
			qntVaretas %= 4

		if qntVaretas >= 2:
			varetasParaFormarRetangulos += 2

	retangulos += varetasParaFormarRetangulos // 4
	print(retangulos)