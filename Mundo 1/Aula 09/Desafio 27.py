print('\033[1;36;40mDESAFIO 27 - AULA 09\033[m\n')
## Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Digite seu nome completo: ').upper().strip()
nome1 = nome.lower().title().split()
print('Seu primeiro nome é: \033[34m{}\033[m'.format(nome1[0]))
print('Seu ultimo nome é: \033[36m{}\033[m'.format(nome1[len(nome1) -1]))
