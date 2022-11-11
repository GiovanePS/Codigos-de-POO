comprimento_estrada, distancia_pedagios = [int(w) for w in input().split()]
custo_por_km, valor_pedagio = [int(w) for w in input().split()]

custo_total = custo_por_km*comprimento_estrada + comprimento_estrada//distancia_pedagios*valor_pedagio

print(custo_total)