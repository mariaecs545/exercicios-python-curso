dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

total = (60 * dias) + (0.15 * km)

print(f'O total a ser pago é R${total:.2f}')
