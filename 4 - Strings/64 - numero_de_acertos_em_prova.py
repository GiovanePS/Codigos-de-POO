gabarito = input()
respostasDadas = input()
acertos = 0

for c in range(len(gabarito)):
    if gabarito[c] == respostasDadas[c]: acertos += 1

print(acertos)