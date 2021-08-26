from desafio import atividade
atividade(67, 15)
## Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.
while True:
    num = int(input('Digite um número: [número negativo para parar] '))
    if num <= 0:
        break
    print('-x-' * 6)
    for contador in range(1, 11):
        print(f'\033[32m{num}\033[m x \033[31m{contador}\033[m = \033[36m{num * contador}\033[m')
    print('-x-' * 6)
