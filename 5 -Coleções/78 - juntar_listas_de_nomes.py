tamanhoLista1 = int(input())
lista1 = [input() for _ in range(tamanhoLista1)]
tamanhoLista2 = int(input())
lista2 = [input() for _ in range(tamanhoLista2)]
uniaoListas = lista1 + lista2
uniaoListas.sort()

for c in uniaoListas: print(c)