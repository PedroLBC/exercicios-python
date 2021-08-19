print('{}DESAFIO 35 - AULA 10{}\n'.format('\033[1;36;40m', '\033[m'))
a = float(input('Coloque o valor da primeira reta: '))
b = float(input('Coloque o valor da segunda reta: '))
c = float(input('Coloque o valor da terceira reta: '))

if a < b + c and b < a + b and c < a + b:
    print('As retas \033[32mPODEM\033[m formar um triangulo!')

else:
    print('As retas \033[31mNÃO PODEM\033[m formar um triangulo!')
