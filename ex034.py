sal = float(input('Salário do funcionário: '))

if sal > 1250.0:
    aum = (sal * 10)/100
    tot = sal + aum
    print(f'Aumento de R${aum:.2f}')
    print(f'Novo Salário: R${tot:.2f}')
else:
    aum = (sal * 15)/100
    tot = sal + aum
    print(f'Aumento de R${aum:.2f}')
    print(f'Novo Salário: R${tot:.2f}')
