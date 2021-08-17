print('\033[1;36;40mDESAFIO 30 - AULA 10\033[m\n')
num = int(input('Coloque um número qualquer: ').strip())

if num % 2 == 0:
    print('\033[32m{}\033[m é um número par!'.format(num))

else:
    print('\033[31m{}\033[m é um número impar!'.format(num))
