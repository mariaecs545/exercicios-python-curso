# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
rq = n ** (1/2)

print(f'O dobro de {n} é {d}')
print(f'O triplo de {n} é {t}')
print(f'A raiz quadrada de {n} é {rq:.2f}')

# OU

print()
n2 = int(input('Digite um número: '))
print(f'O dobro de {n} é {n2 * 2}')
print(f'O triplo de {n} é {n2 * 3}')
print(f'A raiz quadrada de {n} é {pow(n2, (1/2)):.2f}')
