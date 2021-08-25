print('\033[1;36;40mDESAFIO 57 - AULA 13\033[m')

sexo = input('Qual seu gênero? [M / F] ').upper().strip()[0]
while not sexo in 'MF':
    sexo = input('Dado invalido. Por favor, qual seu gênero? [M / F] ').upper().strip()[0]
print('Obrigado!')
