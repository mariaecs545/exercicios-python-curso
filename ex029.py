velo = float(input('Velocidade do veículo (km/h): '))

if velo > 80.0:
    print('Velocidade permitida ultrapassada...')
    print('Calculando valor da multa...')
    multa = (velo - 80) * 7
    print(f'Sua multa é de R${multa:.2f}')
else:
    print('Velocidade adequada.')
