print('\033[1;36;40mDESAFIO 54 - AULA 13\033[m')
## Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
a = 0
b = 0
for c in range(1, 8):
    idade = int(input('Quantos anos você tem? '))
    if idade >= 21:
        a = a + 1
    else:
        b = b + 1
print('{} adultos responderam!'.format(a))
print('{} pessoas jovens respoderam!'.format(b))
