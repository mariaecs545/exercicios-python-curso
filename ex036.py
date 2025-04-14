print('\033[1;34m-' * 30)
print('\033[1;34m     EMPRÉSTIMO BANCÁRIO')
print('\033[1;34m-\033[m' * 30)
print()

valorCasa = float(input('Valor da Casa: R$'))
salario = float(input('Salário: R$'))
anos = int(input('Prazo de Pagamento: '))
print()

max = (salario * 30)/100
mes = anos * 12
parcela = valorCasa/mes

if parcela > max:
    print('\033[1;31mEmpréstimo Negado\033[m')
    print('\033[1;31mValor da parcela excede 30% do salário.\033[m')
else:
    print('\033[1;32mEmpréstimo Aprovado\033[m')
    print(f'Valor da Casa: R${valorCasa:.2f}')
    print(f'Prazo de Pagamento: {anos} anos')
    print(f'Parcelas: R${parcela:.2f} x {mes}')
