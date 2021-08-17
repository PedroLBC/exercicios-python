print('\033[1;36;40mDESAFIO 10 - AULA 07\033[m\n')
## Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
dol = float(input('Converterei o dolar para reais, coloque o valor: '))
real = dol*5.58
print('\033[32m${}\033[m dará \033[31mR${:.2f}\033[m'.format(dol, real))
print('\033[1;33mValor do dolar referente ao dia 11/03/2021 ao horario 12:00\033[m')
