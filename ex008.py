# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

m = float(input('Digite o valor em metros: '))
cm = m * 100
mm = m * 1000

print(f'{m}m = {cm}cm')
print(f'{m}m = {mm}mm')
