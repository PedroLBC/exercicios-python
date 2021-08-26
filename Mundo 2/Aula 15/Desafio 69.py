from desafio import atividade
atividade(69, 15)
## Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

maioridade = homens = mulheres = 0
contagem = 1

while True:
    print('-x-' * 3, f' {contagem} Pessoa ', '-x-' * 3, '\n')
    idade = int(input('Quantos anos você tem? '))
    sexo = input('Qual seu gênero? [H / M] ').upper().strip() [0]
    while not sexo in 'HM':
        sexo = input('Qual seu gênero? [H / M] ').upper().strip() [0]
    contagem += 1

    stop = input('Você quer parar? [S / N] ').upper().strip() [0]
    while not stop in 'SN':
        stop = input('Você quer parar? [S / N] ').upper().strip() [0]
    print()
    
    if idade >= 18:
        maioridade += 1
    
    if sexo == 'H':
        homens += 1
    
    if idade < 20 and sexo == 'M':
        mulheres += 1
    
    if stop == 'S':
        print('Okay...')
        break

print(f'''
    {maioridade} adultos responderam aqui.
    {homens} homens responderam aqui.
    {mulheres} mulheres com menos de 20 anos responderam aqui.
''')
