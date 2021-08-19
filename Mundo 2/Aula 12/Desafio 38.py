print('\033[1;36;40mDESAFIO 38 - AULA 12\033[m\n')
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

## Exercício Python 38: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

if num1 == num2:
    print('{} e {} são o mesmo valor!'.format(num2, num1))

elif num2 > num1:
    print('O {} é maior que {}.'.format(num2, num1))

elif num1 > num2:
    print('O {} é maior que {}.'.format(num1, num2))
