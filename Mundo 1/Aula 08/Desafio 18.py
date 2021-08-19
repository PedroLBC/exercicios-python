from math import radians, sin, cos, tan
print('\033[1;36;40mDESAFIO 18 - AULA 08\033[m\n')
## Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

angulo = float(input('Digite um angulo: '))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print('\033[31mO seno de {} é {:.2f}\033[m\n\033[32mO cosseno de {} é {:.2f}\033[m\n\033[34mO tangente de {} é {:.2f}\033[m'.format(angulo, sen, angulo, cos, angulo, tan))
