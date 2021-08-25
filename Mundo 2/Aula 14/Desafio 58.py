from random import randint

print('\033[1;36;40mDESAFIO 58 - AULA 13\033[m')

print('Explicando: O computador vai escolher um número aleatório entre 0 a 10.')
print('Tente acertar algum número\nVocê tem \033[31m20%\033[m chance de aceitar!')
input('Aperte Enter para continuar: ')

tentativas = 0
cores = 1
numero = int(randint(0, 11))
resposta = int(input('Teste sua sorte: '))

while not numero == resposta:
    if cores == 8:
        cores = 0
    tentativas += 1
    cores += 1
    resposta = int(input('\033[3{}mTeste sua sorte:\033[m '.format(cores)))

print('\033[32mParabéns, você acertou o número!\033[m')
print('\033[31mSuas tentativas foram {}.\033[m'.format(tentativas))