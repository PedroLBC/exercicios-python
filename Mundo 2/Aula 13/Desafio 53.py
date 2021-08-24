frase = input('Digite uma frase: ').strip().lower().replace(' ', '')
inverso = ''
for c in range(len(frase) - 1, -1, -1):
    inverso = inverso + frase[c]

if inverso == frase:
    print('É um palindromo!')
else:
    print("Não é um palindromo!")
