print('\033[1;36;40mDESAFIO 39 - AULA 12\033[m\n')

## Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

idade = int(input('Qual sua idade? '))

if idade == 17 and 18:
    print('Já é hora de entrar no exército!')

elif idade <= 16:
    print('Você tem {} anos para entrar no exército!'.format(abs(idade - 18)))

else:
    print('Já passou do tempo de entrar no exército! Você está {} anos atrasado.'.format(abs(idade - 18)))
