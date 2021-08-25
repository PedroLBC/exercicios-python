from desafio import atividade
atividade(64, 14)
soma = confirmacao = contagem = 0

numero = int(input('Digite um número [999 para parar]: '))
while numero != 999:
    soma += numero
    contagem += 1
    numero = int(input('Digite um número [999 para parar]: '))
print('As vezes antes de parar foram {} e a soma dos valores digitados {}'.format(contagem, soma))
