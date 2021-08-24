from time import sleep
print('\033[1;36;40mDESAFIO 26 - AULA 12\033[m\n')

## Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

salario = float(input('Qual seu salário? R$'))
valorcasa = float(input('Qual o preço da casa? R$'))
emprestimo = float(input('Em quantos anos quer pagar a casa? '))

print('Calculando...')
sleep(2)

if valorcasa / (emprestimo * 12) < salario * (30/100):
    print('\033[32mSeu empréstimo foi aprovado!\033[m')
elif valorcasa / (emprestimo * 12) > salario * (30/100):
    print('\033[31mSeu empréstimo foi recusado por causa do valor mensal '
          'do emprestimo ser maior que 30% do seu salário.\033[m')
