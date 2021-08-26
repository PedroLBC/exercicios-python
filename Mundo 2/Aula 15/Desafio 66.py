from desafio import atividade
atividade(66, 15)

soma = contador = 0

while True:
    num = int(input('Digite um número: [999 para parar] '))

    if num == 999:
        break

    contador += 1
    soma += num

print(f'A soma dos {contador} valores é de {soma}.')
