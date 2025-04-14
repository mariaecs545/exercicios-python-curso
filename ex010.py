# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Digite o valor na carteira em real (R$): '))

dolar = real / 5.72

print()
print(f'Com R${real} pode-se comprar ${dolar:.2f}')
