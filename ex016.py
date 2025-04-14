# Crie um program que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
from math import trunc
num = float(input('Digite um número: '))
print(f'O número {num} tem a parte inteira {trunc(num)}.')

num2 = float(input('Digite outro número: '))
print(f'O número {num2} tem a parte inteira {int(num2)}.')
