from random import choice

print('[1] PEDRA')
print('[2] PAPEL')
print('[3] TESOURA')
jogador = int(input('\033[34mEscolha a sua jogada: \033[m'))

lista = [1, 2, 3]
computador = choice(lista)

if jogador == computador:
    if jogador == 1 and computador == 1:
        print('PEDRA X PEDRA')
    elif jogador == 2 and computador == 2:
        print('PEPEL X PAPEL')
    else:
        print('TESOURA X TESOURA')
    print('\033[33mEMPATE\033[m')
elif jogador == 1 and computador == 2:
    print('PEDRA X PAPEL')
    print('Que pena...')
    print('Vitória \033[34mCOMPUTADOR\033[m')
elif jogador == 1 and computador == 3:
    print('PEDRA X TESOURA')
    print('Parabéns!')
    print('Vitória \033[32mUSUÁRIO\033[m')
elif jogador == 2 and computador == 1:
    print('PAPEL X PEDRA')
    print('Parabéns!')
    print('Vitória \033[32mUSUÁRIO\033[m')
elif jogador == 2 and computador == 3:
    print('PAPEL X TESOURA')
    print('Que pena...')
    print('Vitória \033[34mCOMPUTADOR\033[m')
elif jogador == 3 and computador == 1:
    print('TESOURA X PEDRA')
    print('Que pena...')
    print('Vitória \033[34mCOMPUTADOR\033[m')
elif jogador == 3 and computador == 2:
    print('TESOURA X PAPEL')
    print('Parabéns!')
    print('Vitória \033[32mUSUÁRIO\033[m')
else:
    print('\033[1;31mERROR!\033[m')
    print('Jogada Inválida.')
