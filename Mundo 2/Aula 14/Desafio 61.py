from desafio import atividade
atividade(61, 14)

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