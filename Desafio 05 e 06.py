print('\033[1;36;40mDESAFIO 05 E 06 - AULA 07\033[m')
n = float(input('Coloque um valor: '))
a = n - 1
s = n + 1
m2 = n * 2
m3 = n * 3
d2 = n / 2
d3 = n / 3
p = n ** 2
r = n ** (1/2)
print('\033[1;31mO antecessor é {}\033[m\n\033[1;32mO sucessor é {}\033[m\n\033[1;33mO dobro é {}\033[m\n\033[1;30mO triplo é {}\033[m\n\033[1;34mDivido por 2 é {}\033[m\n\033[1;35mDividido por 3 é {}\033[m\n\033[1;36m{} ao quadrado é {}\033[m\n\033[1;37mA raiz quadrada de {} é {}\033[m'.format(a, s, m2, m3, d2, d3, n, p, n, r))
