# Faça um programa que leia um angulo qualquer e mostre na tela o valor seno, cosseno e tangente desse angulo.
from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tg = tan(radians(ang))

print(f'O ângulo de {ang}° tem o SENO de {sen:.2f}')
print(f'O ângulo de {ang}° tem o COSSENO de {cos:.2f}')
print(f'O ângulo de {ang}° tem a TANGENTE de {tg:.2f}')
