from random import choice
print('\033[1;36;40mDESAFIO 19 - AULA 08\033[m\n')
## Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

print('Referente ao sorteio, coloque o nome dos participantes')
aluno1 = input('Primeiro participante: ')
aluno2 = input('Segundo participante: ')
aluno3 = input('Terceiro participante: ')
aluno4 = input('Quarto participante: ')
aluno5 = input('Quinto participante: ')

r2 = choice([aluno1, aluno2, aluno3, aluno4, aluno5])

print('Entre \033[31m{}, {}, {}, {}, {}\033[m, o sortiado foi \033[32m{}\033[m'.format(aluno5, aluno4, aluno3, aluno2, aluno1, r2))
