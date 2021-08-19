print('\033[1;36;40mDESAFIO 41 - AULA 12\033[m\n')

## Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

idade = int(input('Qual a sua idade? '))

if idade <= 9:
    print('Você é classificado como MIRIM!')

elif idade <= 14:
    print('Você é classificado como INFANTIL!')

elif idade <= 19:
    print('Você é classificado como JÚNIOR!')

elif idade <= 25:
    print('Você é classificado como SÊNIOR!')

else:
    print('Você é classificado como MASTER!')
