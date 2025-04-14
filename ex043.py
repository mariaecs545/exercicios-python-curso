print('\033[1;34m-=' * 10)
print(' CALCULADORA DE IMC')
print('\033[1;34m-=\033[m' * 10)
print()

peso = float(input('Peso (kg): '))
altura = float(input('Altura (m): '))

imc = peso/(altura*altura)
print()

if imc < 18.5:
    print(f'IMC: {imc:.1f}')
    print('\033[31mAbaixo do Peso\033[m')
elif 18.5 <= imc < 25:
    print(f'IMC: {imc:.1f}')
    print('\033[32mPeso Ideal\033[m')
elif 25 <= imc < 30:
    print(f'IMC: {imc:.1f}')
    print('\033[33mSobrepeso\033[m')
elif 30 <= imc < 40:
    print(f'IMC: {imc:.1f}')
    print('\033[31mObesidade\033[m')
else:
    print(f'IMC: {imc:.1f}')
    print('\033[31mObesidade Mórbida\033[m')
