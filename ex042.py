r1 = float(input('Primeira segmento: '))
r2 = float(input('Segunda segmento: '))
r3 = float(input('Terceira segmento: '))
print()

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('Triangulo \033[1;34mEquilátero\033[m')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Triangulo \033[1;34mIsósceles\033[m')
    else:
        print('Triangulo \033[1;34mEscaleno\033[m')
else:
    print('\033[1;31mNÃO pode dormar um triangulo\033[m')
