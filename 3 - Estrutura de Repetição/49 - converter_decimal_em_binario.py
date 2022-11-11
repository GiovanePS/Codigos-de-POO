numeroDecimal = int(input())
numeroBinario = ''

if numeroDecimal != 0:
    while numeroDecimal >= 1:
        if numeroDecimal % 2 == 0:
            numeroBinario = '0'+numeroBinario
            numeroDecimal /= 2
        else:
            numeroBinario = '1'+numeroBinario
            numeroDecimal //= 2
else:
    numeroBinario = '0'

print(numeroBinario)