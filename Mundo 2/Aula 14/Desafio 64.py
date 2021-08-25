from desafio import atividade
atividade(64, 14)
## Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

soma = confirmacao = contagem = 0

numero = int(input('Digite um número [999 para parar]: '))
while numero != 999:
    soma += numero
    contagem += 1
    numero = int(input('Digite um número [999 para parar]: '))
print('As vezes antes de parar foram {} e a soma dos valores digitados {}'.format(contagem, soma))
