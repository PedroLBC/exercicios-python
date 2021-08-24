print('\033[1;36;40mDESAFIO 56 - AULA 13\033[m')
## Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

idadetotal = 0
mulheres = 0
maioridade = 0
nomemaior = ''
for c in range(1, 6):
    print('---- {}ª pessoa ----'.format(c))
    nome = input('Qual seu nome? ')
    idade = float(input('Quantos você tem? '))
    sexo = input('Qual seu sexo? ')
    idadetotal = idadetotal + idade

    if sexo == 'mulher' and idade <= 20:
        mulheres += 1
    if c == 1 and sexo == 'homem':
        maioridade = idade
        nomemaior = nome
    else:
        if idade > maioridade and sexo == 'homem':
            maioridade = idade
            nomemaior = nome

print('A idade média é de {} anos'.format(idadetotal / 5))
print('Tem {} mulheres menores que 20 anos'.format(mulheres))
print('O homem mais velho que respondeu tem {}'.format(nomemaior))
