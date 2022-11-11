import math

num = float(input())
num_NotacaoCientifica = ''

expoente = math.floor(math.log10(abs(num)))

sinal = '+' if expoente >= 0 else '-'

expoente = -expoente
num_NotacaoCientifica += str(round(abs(num*10**expoente), 4))

if num >= 0: num_NotacaoCientifica = '+' + str(f'{float(num_NotacaoCientifica):.4f}')
else: num_NotacaoCientifica = '-' + str(f'{float(num_NotacaoCientifica):.4f}')

print(f'{num_NotacaoCientifica}E{sinal}{abs(expoente):02}')