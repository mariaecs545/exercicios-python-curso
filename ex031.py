d = float(input('Qual a distância em km da sua viagem: '))

if d <= 200.0:
    passagem = d * 0.50
    print(f'Valor da passagem: R${passagem:.2f}')
else:
    passagem = d * 0.45
    print(f'Valor da passagem: R${passagem:.2f}')
