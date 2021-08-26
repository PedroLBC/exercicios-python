from desafio import atividade
atividade(63, 14)
## Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
# Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

contagem = int(input('Qual o termo? '))
num = 1
num1 = 1

print('0 →', end=' ')
while not contagem - 1 <= 0:
    contagem -= 2
    print(num, end=' → ')
    print(num1, end=' → ')
    num += num1
    num1 += num
print('fim')
