print('\033[1;36;40mDESAFIO 29 - AULA 10\033[m\n')
kmh = int(input('Quantos km/h estava? '))

if kmh > 80:
    taxa = (kmh - 80) * 7
    print('Vc estava acima da velocidade permitida, receberá uma \033[31mmulta\033[m de \033[31mR${}\033[m'.format(taxa))

else:
    print('Vc estava na \033[32mvelocidade permitida\033[m, continue assim!')
