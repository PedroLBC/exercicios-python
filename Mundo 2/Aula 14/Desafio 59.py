print('\033[1;36;40mDESAFIO 59 - AULA 14\033[m')

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
lista = [1, 2, 3, 4, 5]
operacoes = 0
cores = 0 

while not operacoes == 7:
    cores += 1             
    print('Qual operação você quer fazer?\n[ 1 ]Adição\n[ 2 ]Subtração\n[ 3 ]Multiplicação'
    '\n[ 4 ]Divisão\n[ 5 ]Potenciação\n[ 6 ]Escolher outros números\n[ 7 ]Sair')  
    operacoes = int(input("Qual sua escolha? "))
    if cores == 8:
        cores = 0 # Sistema de cores
    if operacoes == 1: 
        resultado = n1 + n2 # Adição

    elif operacoes == 2:
        resultado = n1 - n2 # Subtração 
    
    elif operacoes == 3:
        resultado = n1 * n2 # Multiplicação
    
    elif operacoes == 4:
        resultado = n1 / n2 # Divisão
    
    elif operacoes == 5:
        resultado = n1 ** n2 # Potenciação
    
    elif operacoes == 6:
        n1 = int(input('Digite um número: ')) 
        n2 = int(input('Digite outro número: ')) # Mudança de números
    if lista.count(operacoes):
        print('O resultado foi \033[3{}m{:.2f}\033[m'.format(cores, resultado)) # Conclusão + Repetição
