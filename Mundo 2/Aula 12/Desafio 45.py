from random import choice
from time import sleep

print('\033[1;36;40mDESAFIO 45 - AULA 12\033[m\n')

## Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

print('Vamos jogar {}Jo{}ke{}np{}ô!{}\n'.format('\033[31m', '\033[32m', '\033[1;33m', '\033[35m', '\033[m'))
computador = ['tesoura', 'papel', 'pedra']
pessoa = input('Entre:\nPedra \nPapel \nTesoura \nEscolha 1 deles: ').strip().lower()
resultado = choice(computador)
print('\033[1;31mJO...\033[m')
sleep(1)
print('\033[1;32mKEN...\033[m')
sleep(1)
print('\033[1;36mPÔ!\033[m')

if resultado == pessoa:
    print('\033[1;33mOcorreu um empate!\033[m Tente novamente!')

elif pessoa == 'tesoura':
    if resultado == 'papel':
        print('\033[32mParabéns!\033[m\nVc ganhou pois o computador escolheu \033[31m{}\033[m'.format(resultado))
    elif resultado == 'pedra':
        print('\033[31mInfelizmente vc perdeu\033[m. Tente novamente!\n')

elif pessoa == 'papel':
    if resultado == 'pedra':
        print('\033[32mParabéns!\033[m\nVc ganhou pois o computador escolheu \033[31m{}\033[m'.format(resultado))
    elif resultado == 'tesoura':
        print('\033[31mInfelizmente vc perdeu\033[m. Tente novamente!')

elif pessoa == 'pedra':
    if resultado == 'tesoura':
        print('\033[32mParabéns!\033[m\nVc ganhou pois o computador escolheu \033[31m{}\033[m'.format(resultado))
    elif resultado == 'papel':
        print('\033[31mInfelizmente vc perdeu\033[m. Tente novamente!')
