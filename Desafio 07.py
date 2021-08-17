print('\033[1;36;40mDESAFIO 07 - AULA 07\033[m\n')
## Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
nome = input('Olá aluno, qual seu nome? ')
print('\033[32m{}\033[m, farei uma média das suas notas.'.format(nome))
n1 = float(input('Qual nota vc teve no 1 trimestre? '))
n2 = float(input('Qual nota vc teve no 2 trimestre? '))
n3 = float(input('Qual nota vc teve no 3 trimestre? '))
m = (n1 + n2 + n3)/3
print('Sua média é de \033[1;33m{:.2f}\033[m'.format(m))
