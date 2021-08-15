from math import hypot
# from math import sqrt
print('\033[1;36;40mDESAFIO 17 - AULA 08\033[m\n')
b = float(input('Coloque o valor do cateto oposto: '))
c = float(input('Coloque o valor do cateto adjacente: '))
# a = (b ** 2 + c ** 2) ** (1/2)
# a2 = c**2 + b**2
# a = sqrt(a2)
a = hypot(b, c)
print('A hipotenusa é \033[32m{:.2f}\033[m'.format(a))
