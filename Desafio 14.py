print('\033[1;36;40mDESAFIO 14 - AULA 07\033[m\n')
c = float(input('Coloque uma temperatura em Celsius(ºC): '))
print('\033[31mConvertendo para Kelvin dará {}K\033[m\n\033[32mConvervendo para Fahrenheit dará {}ºF\033[m'.format((c + 273.15), ((c * 9/5) + 32)))
input('\n')