# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.

n = int(input('Digite um número: '))

div = f"{n:04d}"
# f"{n:04d}" formata n como uma string de 4 dígitos, adicionando zeros à esquerda se necessário.

print('Milhar:',div[0])
print('Centena:',div[1])
print('Dezena:',div[2])
print('Unidade:',div[3])

# Outra forma:
print()

num = int(input('Digite um número: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Milhar: {m}')
print(f'Centena: {c}')
print(f'Dezena: {d}')
print(f'Unidade: {u}')
