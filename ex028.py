from random import randint
from time import sleep

print('Você consegue adivinhar o número que eu pensei? ')
print('-=-'*20)
n = randint(0, 5)
n2 = int(input('Digite um número entre 0 e 5: '))
print('PROCESSANDO...')
sleep(2)
if n == n2:
    print(f'Parabéns, você acertou! O número era {n}.')
else:
    print(f'Que pena... o número era {n}.')
