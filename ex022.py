# Crie um programa que leia o nome completo de uma pessoa e mostre
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome.

print('-' * 40)
nome = input('Digite o seu nome completo: ').strip()
print('-' * 40)

print('Maiúscula:',nome.upper())
print('Minúscula:',nome.lower())
x = int(len(nome))
y = int(nome.count(' '))
print('Quantidade de letras:',(x - y))
dividido = nome.split()
print('Quantidade de letras do primeiro nome:',len(dividido[0]))
