from random import randint
print('\033[1;36;40mDESAFIO 28 - AULA 10\033[m\n')

print('Explicações: O computador irá escolher um número aleatório entre 0 a 5\nTente adivinhar qual número ele escolheu\nVocê tem \033[31m20%\033[m de chance de acerto!')
input('Aperte a tecla enter para continuar')

numero = int(randint(0, 6))
resposta = int(input('Faça seu chute: '))

if numero == resposta:
    print('\033[32mParabéns, vc acertou o número!\033[m')

elif resposta == '':
    print('\033[33mVc não digitou seu chute!\033[m')

else:
    print('\033[31mPutz, não foi dessa vez!\033[m')
    print('O número era \033[32m{}\033[m'.format(numero))
