while True:
    vezesJogadas = int(input())
    if vezesJogadas == 0: break
    jogoAtual = [int(x) for x in input().split(' ')]
    print(f'Mary won {jogoAtual.count(0)} times and John won {jogoAtual.count(1)} times')