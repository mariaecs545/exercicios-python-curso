# Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome.

nome = input('Digite o seu nome completo: ').strip()

proc = 'SILVA' in nome.upper()

print('Tem Silva no nome?',proc)
