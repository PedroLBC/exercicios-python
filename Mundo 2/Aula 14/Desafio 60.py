from desafio import atividade
atividade(60, 14)
## Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. 
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

number = resultado = int(input('Digite um número: '))

while not number == 1:
    number -= 1
    resultado *= number 
print('Seu número calculado em fatorial é: {}'.format(resultado))
