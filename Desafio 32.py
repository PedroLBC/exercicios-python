print('\033[1;36;40mDESAFIO 32 - AULA 10\033[m\n')
ano = int(input('Digite um ano: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('É um \033[32mano bissexto\033[m!')

elif ano % 4 == 1:
    print('Não é um \033[31mano bissexto\033[m, mas em \033[32m{}\033[m será!'.format(ano + 3))

elif ano % 4 == 2:
    print('Não é um \033[31mano bissexto\033[m, mas em \033[32m{}\033[m será!'.format(ano + 2))

else:
    print('Não é um \033[31mano bissexto\033[m, mas em \033[32m{}\033[m será!'.format(ano + 1))
