txtFinal = ''
while True:
    saida = 'BUG'
    try:
        frase = input().upper().split('-')
        if len(frase) != 5: raise EOFError
        if 'C' in frase[0][0] or 'C' in frase[0][-1]:
            if 'O' in frase[1][0] or 'O' in frase[1][-1]:
                if 'B' in frase[2][0] or 'B' in frase[2][-1]:
                    if 'O' in frase[3][0] or 'O' in frase[3][-1]:
                        if 'L' in frase[4][0] or 'L' in frase[4][-1]:
                            saida = 'GRACE HOPPER'
        txtFinal += saida+'\n'
    except EOFError: break

print(txtFinal, end='')