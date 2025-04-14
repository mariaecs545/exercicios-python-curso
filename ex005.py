# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número: '))
a = n - 1
s = n + 1
print(f'O sucessor de {n} é {s}')
print(f'O antecessor de {n} é {a}')
print()

n2 = int(input('Digite um número: '))
print(f'Analisando o número {n2}, seu antecessor é {n2 - 1} e o seu sucessor é {n2 + 1}.')
