from desafio import atividade
atividade(63, 14)

contagem = int(input('Qual o termo? '))
num = 1
num1 = 1

print('0 →', end=' ')
while not contagem - 1 <= 0:
    contagem -= 2
    print(num, end=' → ')
    print(num1, end=' → ')
    num += num1
    num1 += num
print('fim')
