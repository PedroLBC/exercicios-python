print('DESAFIO 04 - AULA 06\n')
a = input('Digite algo: ')
print('Refente a o que preencheu:')
print('')
print('O tipo é:',type(a))
print('')
print('É uma letra? ',a.isalpha())
print('')
print('É um numeral? ',a.isnumeric())
print('')
print('É uma letra númerica? ',a.isalnum())
print('')
print('É ASCII? ',a.isascii())
print('')
print('É um digito? ',a.isdigit())
print('')
print('É decimal? ',a.isdecimal())
print('')
print('E um identificador? ',a.isidentifier())
print('')
print('Está em minúsculo? ',a.islower())
print('')
print('Está em maiúsculo? ',a.isupper())
print('')
print('É impresso? ',a.isprintable())
print('')
print('É titlecased? ',a.istitle())
print('')
print('É um espaço(tecla)? ',a.isspace())
print('')
print('É {} gay? True'.format(a))
input('\n')