import desafio
desafio.atividade(65, 14)

confirmação = contagem_media = soma = 0
contagem = 5

numero = maior = menor = int(input('Digite um número: '))

while not confirmação == 1:
    numero = int(input('Digite um número: '))
    contagem -= 1
    contagem_media += 1
    soma += numero

    if numero < maior:
        maior = numero
    
    if numero > menor:
        menor = numero
    
    if contagem == 1: 
        contagem = int(input('Quer continuar por mais quantas vezes? [0 para parar] '))
    
    if contagem == 0:
        confirmação = 1

media = soma / contagem_media
print('A média foi {}'.format(media))
print('O maior número foi {} e o menor número foi {}'(maior, menor))