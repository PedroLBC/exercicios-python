print('\033[1;36;40mDESAFIO 15 - AULA 07\033[m\n')
## Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dia = float(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos km foram percorridos com o carro? '))
v1 = dia * 60
v2 = km * 0.15
todo = v1 + v2
print('\033[31mSeus dias custaram {}\033[m\n\033[32mSeus km percorridos custaram {}\033[m\n\033[34mAo todo ficou {}\033[m'.format(v1, v2, todo))
