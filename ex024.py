# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = input('Digite o nome de uma cidade: ').strip()

div = cidade.split()

comp = (div[0].upper() == 'SANTO')
print('Começa com a palavra Santo?',comp)
