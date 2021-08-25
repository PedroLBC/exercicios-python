print('\033[1;36;40mDESAFIO 49 - AULA 13\033[m')
## Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Set a number: '))

for c in range(1, 11):
    print('{} x {} = {}'.format(num, c, (num * c)))
