print('\033[1;36;40mDESAFIO 13 - AULA 07\033[m\n')
## Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
sal = float(input('Qual seu salário atual? '))
sal10 = sal/10
sal5 = sal10/2
sal15 = sal10 + sal5
sal5p = sal5 + sal
sal10p = sal10 + sal
sal15p = sal15 + sal
print('\033[31mCom 5% de aumento salárial dará {}\033[m\n\033[32mCom 10% de aumento salárial dará {}\033[m\n\033[34mCom 15% de aumento salárial dará {}\033[m'.format(sal5p, sal10p, sal15p))
input('\n')
