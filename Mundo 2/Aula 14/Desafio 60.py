from desafio import atividade
atividade(60, 14)

number = resultado = int(input('Digite um número: '))

while not number == 1:
    number -= 1
    resultado *= number 
print('Seu número calculado em fatorial é: {}'.format(resultado))
