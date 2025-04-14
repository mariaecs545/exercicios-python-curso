# Desenvolva um programa que leia as duas notas de um aluno. Calcule a média.

print('---------- ESCOLA ----------')

student = input('Digite o nome do aluno: ')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2

print('---------- MÉDIA ----------')
print(f'A média do aluno(a) {student} é {m:.1f}')
