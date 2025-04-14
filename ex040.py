print('\033[1;34m-=' * 10)
print(' CHECAGEM DE NOTAS')
print('\033[1;34m-=\033[m' * 10)
print()

nome = str(input('Nome do Aluno(a): '))
n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
print()

media = (n1 + n2)/2

print(f'Aluno(a): {nome}')
print(f'Média do aluno(a): {media:.1f}')

if media < 5.0:
    print('\033[1;31mAluno Reprovado.\033[m')
elif 5.0 <= media < 7:
    print('\033[1;33mAluno de Recuperação.\033[m')
else:
    print('\033[1;32mAluno Aprovado.\033[m')
