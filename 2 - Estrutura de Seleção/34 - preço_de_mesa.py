comprimento = float(input())
largura = float(input())
numeroDeGavetas = int(input())
tipoDeMadeira = input()

precoDaMesa = largura*comprimento*100
	
if largura*comprimento > 2:
	precoDaMesa += 50
	
if tipoDeMadeira == 'mogno':
	precoDaMesa += 150
elif tipoDeMadeira == 'carvalho':
	precoDaMesa += 125
	
precoDaMesa += 30*numeroDeGavetas

if precoDaMesa < 200:
	print(200.00)
else:
	print(f'{precoDaMesa:.2f}')