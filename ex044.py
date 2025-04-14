print('========== LOJAS TITA ==========')
produto = float(input('Valor das compras: R$'))
print()

print('\033[4mForma de Pagamento:\033[m ')
print('[1] \033[34mDinheiro/Cheque\033[m')
print('[2] À Vista no \033[34mCartão\033[m')
print('[3] \033[31m2x\033[m no \033[34mCartão\033[m')
print('[4] \033[31m3x ou mais\033[m no \033[34mCartão\033[m')
forma = int(input('Escolha a forma de pagamento: '))
print()

if forma == 1:
    desconto = (produto*10)/100
    tot = produto - desconto
    print(f'\033[32mDesconto de R${desconto:.2f}\033[m')
    print(f'Total: R${tot:.2f}')
elif forma == 2:
    desconto = (produto*5)/100
    tot = produto - desconto
    print(f'\033[32mDesconto de R${desconto:.2f}\033[m')
    print(f'Total: R${tot:.2f}')
elif forma == 3:
    print(f'Total: R${produto:.2f}')
elif forma == 4:
    parcelas = int(input('Quantas parcelas? '))
    juros = (produto*20)/100
    tot = produto + juros
    pt = tot / parcelas
    print(f'\033[31mAcréscimo de R${juros:.2f}\033[m')
    print(f'{parcelas} x de R${pt:.2f}')
    print(f'Total: R${tot:.2f}')
else:
    print('\033[1;31mERROR!\033[m')
    print('Forma de pagamento não identificada.')
