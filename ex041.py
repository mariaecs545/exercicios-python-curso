from datetime import date

print('\033[1;34m-=' * 16)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('\033[1;34m-=\033[m' * 16)
print()

ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano

print(f'Idade do atleta: {idade} anos')
if idade <= 9:
    print('Categoria: \033[1;31mMIRIM\033[m')
elif idade <= 14:
    print('Categoria: \033[1;31mINFANTIL\033[m')
elif idade <= 19:
    print('Categoria: \033[1;31mJUNIOR\033[m')
elif idade <= 25:
    print('Categoria: \033[1;31mSÊNIOR\033[m')
else:
    print('Categoria: \033[1;31mMASTER\033[m')
