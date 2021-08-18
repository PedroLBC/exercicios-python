print('\033[1;36;40mDESAFIO 26 - AULA 09\033[m\n')
## Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = input('Digite uma frase: ').strip()
frase1 = frase.upper()
print('Na frase aparece a letra "a" \033[36m{}\033[m vez(es)'.format(frase1.count('A')))
print('Na frase a primeira letra "a" esta no caractere \033[34m{}\033[m'.format(frase1.find('A')+1))
print('Na frase a ultima letra "a" esta no caractere \033[35m{}\033[m'.format(frase1.rfind('A')+1))
