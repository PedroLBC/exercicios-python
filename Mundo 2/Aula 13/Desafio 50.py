print('\033[1;36;40mDESAFIO 50 - AULA 13\033[m')

soma = 0

for c in range(1, 7):
    num = int(input('Coloque um número: '))
    if num % 2 == 0:
        soma += num

print('A soma dos números pares foi {}'.format(soma))
