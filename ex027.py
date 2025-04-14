# Nome completo, primeiro e último nome.

print('-' * 40)
n = str(input('Digite o seu nome completo: ')).strip()
print('-' * 40)

nome = n.split()

print(f'Primeiro nome: {nome[0]}')
print(f'Segundo nome: {nome[len(nome) - 1]}')
