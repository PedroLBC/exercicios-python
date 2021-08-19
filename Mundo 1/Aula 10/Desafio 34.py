print('{}DESAFIO 34 - AULA 10{}\n'.format('\033[1;36;40m', '\033[m'))
salario = float(input('Qual seu salário? '))

if salario >= 1250:
    print('Seu salário atual será de \033[32m{}\033[m por conta do aumento salarial de 10% concebido!'.format(salario + (salario * (10/ 100))))

else:
    print('Seu salário atual será de \033[32m{}\033[m por conta do aumento salarial de 15% concebido!'.format(salario + (salario * (15/ 100))))
