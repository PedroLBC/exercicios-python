print('\033[1;36;40mDESAFIO 43 - AULA 12\033[m')

## Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

alturastring = input("Qual sua altura? ").replace(',', '.')
pesostring = input("Qual seu peso? ").replace(',', '.')
altura = float(alturastring)
peso = float(pesostring)

imc = peso / (altura ** 2)

print('Seu IMC é de: {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso!')

elif imc <= 25:
    print('Você está no peso ideal!')

elif imc <= 30:
    print('Você está com sobrepeso!')

elif imc <= 40:
    print('Você está obeso!')

else:
    print('Você está com obesidade mórbida!')
