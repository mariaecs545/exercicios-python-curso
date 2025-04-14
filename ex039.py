from datetime import date

nasc = int(input('Ano de nascimento: '))
atual = date.today().year

idade = atual - nasc
falta = 18 - idade
passou = idade - 18

print(f'Você nasceu em {nasc}. Tem {idade} anos em {atual}.')
print()
if idade < 18:
    print('\033[1;32mAinda vai se alistar.\033[m')
    print(f'Faltam {falta} anos para o seu alistamento.')
    print(f'Ano de alistamento: {atual + falta}')
elif idade == 18:
    print('\033[1;33mHora de se alistar!\033[m')
else:
    print('\033[1;31mPassou do tempo de alistamento.\033[m')
    print(f'{passou} anos depois do prazo.')
    print(f'Ano de alistamento: {atual - passou}')
