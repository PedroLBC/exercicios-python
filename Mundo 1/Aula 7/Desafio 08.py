print('\033[1;36;40mDESAFIO 08 - AULA 07\033[m\n')
## Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
metro = float(input('Coloque um valor em metros: '))
km = metro/1000
cent = metro*100
mili = metro*1000
print('\033[31mConvertendo para centimetros dará {}cm\033[m\n\033[32mConvertendo para milimetros dará {}mm\033[m\n\033[34mConvertendo para quilometros dará {}km\033[m'.format(cent, mili, km))
