print('\033[1;36;40mDESAFIO 33 - AULA 10\033[m\n')

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

if num1 > num2:
    if num1 > num3:
        if num2 > num3:
            print(f'Respectivamente do maior para o menor: \033[32m{num1}, {num2} e {num3}\033[m')
        else:
            print(f'Respectivamente do maior para o menor: \033[32m{num1}, {num3} e {num2}\033[m')
    else:
        print(f'Respectivamente do maior para o menor: \033[32m{num3}, {num1} e {num2}\033[m')

elif num2 > num1:
    if num2 > num3:
        if num1 > num3:
            print(f'Respectivamente do maior para o menor: \033[32m{num2}, {num1} e {num3}\033[m')
        else:
            print(f'Respectivamente do maior para o menor: \033[32m{num2}, {num3} e {num1}\033[m')
    else:
        print(f'Respectivamente do maior para o menor: \033[32m{num3}, {num2} e {num1}\033[m')
