print('\033[1;36;40mDESAFIO 51 - AULA 13\033[m')
## Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
num = int(input('Qual o primeiro termo? '))
raz = int(input('Qual a razão? '))
dec = num + (10 - 1) * raz
for c in range(num, dec + raz, raz):
    print(c, end=' -> ')
print('etc.')
