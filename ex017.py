# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo, calcule e mostre o comprimento da hipotenusa.
from math import sqrt
co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))
h = sqrt((co**2)+(ca**2))
# h = math.hypot(co, ca)

print(f'A hipotenusa é igual a {h:.2f}.')
