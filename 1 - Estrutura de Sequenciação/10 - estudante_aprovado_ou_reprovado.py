nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
peso1 = float(input())
peso2 = float(input())
peso3 = float(input())

media_final = (nota1*peso1 + nota2*peso2 + nota3*peso3) / (peso1+peso2+peso3)

print(media_final >= 6)