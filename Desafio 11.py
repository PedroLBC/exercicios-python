print('\033[1;36;40mDESAFIO 11 - AULA 07\033[m\n')
com = float(input('Referente a uma parede, qual o comprimento dela (em metros)? '))
larg = float(input('E a largura (em metros)? '))
area = com * larg
litros = area / 2
print('A parede tem uma área de \033[31m{}\033[m e precisaria de \033[32m{}L\033[m de tinta para pintala'.format(area, litros))
print('\033[1;33mConsiderando 1L = 2m²\033[m')
