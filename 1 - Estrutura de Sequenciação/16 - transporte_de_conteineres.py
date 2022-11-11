conteiner_largura, conteiner_comprimento, conteiner_altura = [int(w) for w in input().split()]
navio_largura, navio_comprimento, navio_altura = [int(w) for w in input().split()]

total_conteineres = (navio_largura//conteiner_largura) * (navio_comprimento//conteiner_comprimento) * (navio_altura//conteiner_altura)

print(total_conteineres)