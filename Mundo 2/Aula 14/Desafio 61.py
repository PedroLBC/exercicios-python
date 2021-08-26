from desafio import atividade
atividade(61, 14)
## Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

num = int(input('Qual o primeiro termo? '))
raz = int(input('Qual a razão? '))
confirmacao = 1
contagem = 10
while not confirmacao == 0:
    contagem -= 1
    if contagem == 0:
        confirmacao = 0
    print(num, '→ ', end='')
    num += raz
print('etc.')
