print('\033[1;36;40mDESAFIO 23 - AULA 09\033[m\n')
## Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

inteiro = int(input('Coloque um numero entre 0 a 9999: '))
if inteiro <= 9:
    print('\033[35mUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}\033[m'.format(inteiro, 0, 0, 0))

elif inteiro <= 99:
    letra = str(inteiro)
    print('\033[35mUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}\033[m'.format(letra[1], letra[0], 0, 0))

elif inteiro <= 999:
    letra = str(inteiro)
    print('\033[35mUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}\033[m'.format(letra[2], letra[1], letra[0], 0))

elif inteiro <= 9999:
    letra = str(inteiro)
    print('\033[35mUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}\033[m'.format(letra[3], letra[2], letra[1], letra[0]))

else:
    print('\033[31mSeu número saiu da margem predefinida na mensagem anterior\033[m')
