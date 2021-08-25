from desafio import atividade
atividade(62, 14)

num = int(input('Qual o primeiro termo? '))
raz = int(input('Qual a razão? '))
contagem = int(input('Com quantas vezes você quer que a PA apareça? ')) + 1
while not contagem == 0:
    contagem -= 1
    print(num, '→ ', end='')
    num += raz
    if contagem == 1:
        print('Pausado')
        contagem = int(input('\nCom quantas vezes você quer que a PA apareça? [0 para parar] ')) + 1
        if contagem == 1:
            contagem = 0
