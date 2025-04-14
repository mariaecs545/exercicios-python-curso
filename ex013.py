# Faça um algoritmo que leia o salário de funcionário e mostre o seu novo salário com 15% de aumento.

f = input('Nome do Funcionário: ')
s1 = float(input('Salário: R$'))

aumento = (s1 * 15) / 100
s2 = s1 + aumento

print(f'Novo Salário: R${s2:.2f}')
