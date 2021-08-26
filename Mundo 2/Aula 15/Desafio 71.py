from desafio import atividade
atividade(71, 15)
## Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. 
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

num = int(input('Qual o valor que você quer sacar? R$'))

cedula50 = num // 50
cedula20 = cedula50 // 20
cedula10 = cedula20 // 10
cedula1 = cedula10 // 1

cedula50a = num % 50
cedula20a = cedula50a % 20
cedula10a = cedula20a % 10
cedula1a = cedula10a % 1


print('Resultado: ')
if num >= 50:
    print('Notas de 50 -',num // 50) # pra 50

    if (cedula50a % 20) <= 20:
        calculo20 = cedula50 // 20 # pra 20
        print('Notas de 20 -',calculo20)

    if (cedula20a % 10) <= 10:
        calculo10 = cedula20a // 10 # pra 10
        print('Notas de 10 -',calculo10)

    if (cedula10a % 1) <= 1:
        calculo1 = cedula10a // 1 # pra 1
        print('Notas de 1 - ',calculo1)

if num <= 49 and num >= 20:
    print('Notas de 20 -',num // 20) # até 20
    if (cedula20a % 10) <= 10:
        calculo10 = cedula20a // 10 # pra 10
        print('Notas de 10 -',calculo10)

    if (cedula10a % 1) <= 1:
        calculo1 = cedula10a // 1 # pra 1
        print('Notas de 1 -',calculo1)

if num <= 19 and num >= 10:
    print('Notas de 10 -',num // 10) # até 10
    if (cedula10a % 1) <= 1:
        calculo1 = cedula10a // 1 # pra 1
        print('Notas de 1 -',calculo1)

if num <= 9:
    print('Notas de 1 -',num // 1) # 9 ou -
