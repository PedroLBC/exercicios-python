print('\033[1;36;40mDESAFIO 57 - AULA 13\033[m')
## Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input('Qual seu gênero? [M / F] ').upper().strip()[0]
while not sexo in 'MF':
    sexo = input('Dado invalido. Por favor, qual seu gênero? [M / F] ').upper().strip()[0]
print('Obrigado!')
