from math import trunc
# from math import floor, ceil
print('\033[1;36;40mDESAFIO 16 - AULA 07\033[m\n')
num = float(input('Digite um número: '))
# print('Floor: {}\nCeil: {}'.format(floor(num), ceil(num)))
# print('O valor inteiro é {}'.format(int(num)))  /// int quase = ao trunc
print('O valor inteiro é \033[32m{}\033[m'.format(trunc(num)))