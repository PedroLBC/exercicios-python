print('\033[1;36;40mDESAFIO 48 - AULA 13\033[m')

soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
print('a soma é de: {}'.format(soma))
