from random import randint

print('\033[1;36;40mDESAFIO 58 - AULA 13\033[m')
## Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
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
