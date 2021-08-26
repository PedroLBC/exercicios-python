from desafio import atividade
atividade(70, 15)
## Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

soma = maior_preco = menor_preco = contador = 0
nome_menor_preco = ''

while True:
    nome = input("Qual o nome do produto? ")
    preco = int(input("Qual o preço do produto? R$"))

    contador += 1
    soma += preco

    if preco > 1000:
        maior_preco += 1

    if contador == 1:
        menor_preco = preco
        nome_menor_preco = nome
    if preco < menor_preco:
        menor_preco = preco
        nome_menor_preco = nome

    stop = input('Você quer parar? [S / N] ').upper() [0]
    while not stop in 'SN':
        stop = input('Você quer parar? [S / N] ').upper() [0]
    if stop == 'S':
        print('Okay...')
        break

print(f'''
O preço total foi R${soma}
Temos {maior_preco} produto(s) custando mais que R$1000
O produto mais barato é {nome_menor_preco} que custa R${menor_preco}
''')
