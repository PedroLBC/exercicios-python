print('\033[1;36;40mDESAFIO 55 - AULA 13\033[m')
maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input('Qual seu peso? '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O menor peso lido foi {}'.format(menor))
print('O maior peso lido foi {}'.format(maior))
