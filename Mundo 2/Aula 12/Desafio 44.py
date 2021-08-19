print('\033[1;36;40mDESAFIO 44 - AULA 12\033[m\n')

## Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

produto = float(input('Qual o valor do produto? '))
pagamento = input('Qual a forma de pagamento? ').strip().lower().replace(' ', '')

if pagamento == 'dinheiro' or 'cheque':
    print('O produto recebeu 10% de desconto pela forma de pagamento, '
          'assim passando a valer R${}'.format(produto - (produto * (10 / 100)))) # dinheiro 10%

elif pagamento == 'cartão' or 'cartao' or 'credito' or 'debito' or 'crédito' or 'débito':
    vista = input('Quer pagar à vista? ').strip().lower()
    if vista == 'sim':
        print('O produto recebeu 5% de desconto pela forma de pagamento, '
              'assim passando a valer R${}'.format(produto - (produto * (5 / 100))))
    else:
        vezes = int(input('APENAS em números, quantas vezes quer pagar? '))
        if vezes == 2:
            print('Por parcelar em 2 vezes, o produto manterá o mesmo valor!')
        else:
            print('Por parcelar em {} vezes, haverá juros, '
                  'com o produto final valendo R${}'.format(vezes, produto + (produto * (20/100))))
