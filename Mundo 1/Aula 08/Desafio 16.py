from math import trunc
print('\033[1;36;40mDESAFIO 16 - AULA 07\033[m\n')
## Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

num = float(input('Digite um número: '))
print('O valor inteiro é \033[32m{}\033[m'.format(trunc(num)))
