print('\033[1;36;40mDESAFIO 40 - AULA 12\033[m\n')

## Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

n1 = float(input('Qual foi sua nota no 1º trimestre? '))
n2 = float(input('Qual foi sua nota no 2º trimestre? '))
n3 = float(input('Qual foi sua nota no 3º trimestre? '))
media = (n1 + n2 + n3)/3
print('Sua média é {:.2f}'.format(media))

if media <= 4:
    print('Sua média está muito baixa, infelizmente você reprovou!')

elif media <= 6.9:
    print('Foi por pouco, mas terá outra chance com a recuperação, não vacile!')

else:
    print('Parabéns! Você foi aprovado!')
