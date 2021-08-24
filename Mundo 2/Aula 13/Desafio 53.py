print('\033[1;36;40mDESAFIO 53 - AULA 13\033[m')
## Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
# ex.: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
frase = input('Digite uma frase: ').strip().lower().replace(' ', '')
inverso = ''
for c in range(len(frase) - 1, -1, -1):
    inverso = inverso + frase[c]

if inverso == frase:
    print('É um palindromo!')
else:
    print("Não é um palindromo!")
