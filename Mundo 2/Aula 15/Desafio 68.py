from random import randint
from cores import clean, green, red, yellow
from desafio import atividade 
atividade(68, 15)
## Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

contagem = 0

while True:
    par_impar = input('Par ou impar? [P / I] ').upper() [0]
    while not par_impar in 'PI':
        par_impar = input('Odds or evens? [P / I] ').upper() [0]
    pc = randint(0, 11)
    num = int(input('Escolha um número: '))
    soma = num + pc
    if soma % 2 == 0:
        if par_impar == 'I':
            print(f'{red()}Você perdeu!{clean()}')
            break

        if par_impar == 'P':
            print(f'{green()}Você ganhou!{clean()}')
            contagem += 1
    
    if soma % 2 != 0:
        if par_impar == 'P':
            print(f'{red()}Você perdeu!{clean()}')
            break

        if par_impar == 'I':
            print(f'{green()}Você ganhou!{clean()}')
            contagem += 1

print(f'Suas vitórias consecutivas foram de {yellow()}{contagem}{clean()}')
