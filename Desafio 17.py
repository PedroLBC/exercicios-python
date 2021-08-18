from math import hypot
print('\033[1;36;40mDESAFIO 17 - AULA 08\033[m\n')
## Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
# Calcule e mostre o comprimento da hipotenusa.

b = float(input('Coloque o valor do cateto oposto: '))
c = float(input('Coloque o valor do cateto adjacente: '))
a = hypot(b, c)
print('A hipotenusa é \033[32m{:.2f}\033[m'.format(a))
