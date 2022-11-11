qntDisciplinas = int(input())

entrada = [[x for x in input().split()] for _ in range(qntDisciplinas)]
grade = [[None for _ in range(6)] for n in range(14)]

choque = False
for c in range(len(entrada)):
    linha = entrada[c]
    materia = linha[0]
    horarios = linha[1:]
    mapeamento = ['0730', '0820', '0910', '1010', '1100', '1330', '1420', '1510', '1620', '1710', '1830', '1920', '2020', '2110']
    
    for x in horarios:
        diaDaSemana = int(x[0])
        hora = x[1:5]
        qntAulas = int(x[5])
        for y in range(qntAulas):
            if grade[mapeamento.index(hora)+y][diaDaSemana-2] == None:
                grade[mapeamento.index(hora)+y][diaDaSemana-2] = materia
            else:
                print(grade[mapeamento.index(hora)+y][diaDaSemana-2], materia)
                choque = True
                break
        if choque: break
    if choque: break