print('\033[1;36;40mDESAFIO 42 - AULA 12\033[m\n')

## Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

a = float(input('Digite o valor do primeiro lado: '))
b = float(input('Digite o valor do segundo lado: '))
c = float(input('Digite o valor do terceiro lado: '))

if a < b + c and b < a + b and c < a + b:
    print('Os lado PODEM formar um triângulo!')
    if a == b and b == c:
        print('E um triangulo EQUILÁTERO!')
    elif a == b or b == c or a == c:
        print('E um triangulo ISÓSCELES!')
    else:
        print('E um triangulo ESCALENO!')

else:
    print("Os lados NÃO PODEM formar um triângulo!")
