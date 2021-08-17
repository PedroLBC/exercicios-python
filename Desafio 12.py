print('\033[1;36;40mDESAFIO 12 - AULA 07\033[m\n')
## Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
nopromo = float(input('Qual o valor do produto sem desconto? '))
promo10 = nopromo/10
promo5 = promo10/2
promo20 = promo10*2
promo30 = promo10*3
promo5p = nopromo - promo5
promo10p = nopromo - promo10
promo20p = nopromo - promo20
promo30p = nopromo - promo30
print('\033[31mCom 5% de desconto dará {}\033[m\n\033[32mCom 10% de desconto dará {}\033[m\n\033[34mCom 20% de desconto {}\033[m\n\033[35mCom 30% de desconto {}\033[m'.format(promo5p, promo10p, promo20p, promo30p))
