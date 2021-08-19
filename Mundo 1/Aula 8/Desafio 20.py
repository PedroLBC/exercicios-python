from random import sample

print('\033[1;36;40mDESAFIO 20 - AULA 08\033[m\n')
## Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

print('Referente aos grupos que irão apresentar, coloque o nome deles: \nOBS:apenas 3 serão selecionados pela falta de horario da aula')
grupo1 = input('Nome do primeiro grupo: ')
grupo2 = input('Nome do segundo grupo: ')
grupo3 = input('Nome do terceiro grupo: ')
grupo4 = input('Nome do quarto grupo: ')

resultado1 = sample([grupo1, grupo2, grupo3, grupo4], k=3)

print('Entre \033[31m{}, {}, {}, {}\033[m, os sortiados foram \033[32m{}\033[m'.format(grupo2, grupo3, grupo1, grupo4, resultado1))
