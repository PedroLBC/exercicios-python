from desafio import atividade
atividade(67, 15)

while True:
    num = int(input('Digite um número: [número negativo para parar] '))
    if num <= 0:
        break
    print('-x-' * 6)
    for contador in range(1, 11):
        print(f'\033[32m{num}\033[m x \033[31m{contador}\033[m = \033[36m{num * contador}\033[m')
    print('-x-' * 6)
