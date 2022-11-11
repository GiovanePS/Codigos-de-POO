A = int(input())
B = int(input())
C = int(input())

if A == B == C:
    print('equilátero')
elif A == B or B == C or A == C:
    print('isósceles')
else:
    print('escaleno')