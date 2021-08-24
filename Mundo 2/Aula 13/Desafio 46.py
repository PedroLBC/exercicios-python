from time import sleep
print('\033[1;36;40mDESAFIO 46 - AULA 13\033[m')

print('A contagem começa em 10 segundos!')
for c in range(10, 0, -1):
    n = c
    if c == 10:
        n = 1
    elif c == 9:
        n = 2
    elif c == 8:
        n = 3
    print('\033[3{}m{}...\033[m'.format(n, c))
    sleep(1)
print('Feliz Ano Novo!')
