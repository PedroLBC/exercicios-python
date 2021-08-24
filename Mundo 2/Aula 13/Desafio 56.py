print('\033[1;36;40mDESAFIO 56 - AULA 13\033[m')

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
