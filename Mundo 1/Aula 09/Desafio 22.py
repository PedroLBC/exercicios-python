print('\033[1;36;40mDESAFIO 22 - AULA 09\033[m\n')
## Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome = input('Coloque seu nome completo: ').strip()
print('Seu nome apenas em letras minúsculas: \033[32m{}\033[m'.format(nome.lower()))
print('Seu nome apenas em letras maiúsculas: \033[31m{}\033[m'.format(nome.upper()))
# nomes = nome.replace(' ', '')
print('Quantidade de letras existentes no seu nome: \033[34m{}\033[m'.format(len(nome.replace(' ', ''))))
nomess = nome.split()
print('Quantidade de letras existentes no seu primeiro nome: \033[36m{}\033[m'.format(len(nomess[0])))
