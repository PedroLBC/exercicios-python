print('\033[1;36;40mDESAFIO 25 - AULA 09\033[m\n')
## Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = input('Coloque seu nome completo: ')
NOME = nome.upper()
print('No seu nome há \033[33mSilva\033[m?')
print('SILVA' in NOME)
