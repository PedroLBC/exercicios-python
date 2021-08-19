print('\033[1;36;40mDESAFIO 31 - AULA 10\033[m\n')
km = float(input('Quantos km é a viagem? '))

if km <= 199:
    taxa = km * 0.50

else:
    taxa = km * 0.45

print('O valor da passagem é de \033[31mR${}\033[m'.format(taxa))
