print('\033[1;36;40mDESAFIO 37 - AULA 12\033[m\n')

## Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Coloque um número: '))
print('Eu vou converter esse número para binário, octal ou hexadecimal!\n')
print('Converterei o número para o escolhido:\nPara binário responda com "1"')
converter = int(input('Para binário responda com "2"\nPara binário responda com "3"\nSua opção: '))

if converter == 1:
    print('Seu número convertido para binário é: {}'.format(bin(num)[2:]))

elif converter == 2:
    print('Seu número convertido para octal é: {}'.format(oct(num)[2:]))

elif converter == 3:
    print('Seu número convertido para hexadecimal é: {}'.format(hex(num)[2:]))

else:
    print("Sua opção foi invalida!")

resultado = input('Você quer ver as outras opções com o mesmo número? ').strip().lower()

if resultado == 'sim' or resultado == 'yes':
    print('Isso é bom!\nBinário: {}\nOctal: {}\nHexadecimal: {}'.format(bin(num)[2:], oct(num)[2:], hex(num)[2:]))

else:
    print('Ok.')
