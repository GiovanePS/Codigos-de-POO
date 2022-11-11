while True:
    eh_tautagrama = True
    frase = input()
    if frase == '*': break
    fraseLista = frase.upper().split(' ')
    for c in fraseLista:
        if fraseLista.index(c) == 0:
            LetraTautagrama = c[0]
        if c[0] == LetraTautagrama:
            continue
        else:
            eh_tautagrama = False
            break
    if eh_tautagrama: print('Y')
    else: print('N')