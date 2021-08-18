print('\033[1;36;40mDESAFIO 24 - AULA 09\033[m\n')
## Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Qual o nome da sua cidade? ')).strip()
CIDADE = cidade.upper()
cidade1 = CIDADE.lower().title()
print('Em \033[32m{}\033[m começa com o nome \033[33mSanto\033[m?'.format(cidade1))
print(CIDADE[0:5] == 'SANTO')
