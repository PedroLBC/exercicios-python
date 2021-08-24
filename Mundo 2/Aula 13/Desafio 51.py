num = int(input('Qual o primeiro termo? '))
raz = int(input('Qual a razão? '))
dec = num + (10 - 1) * raz
for c in range(num, dec + raz, raz):
    print(c, end=' -> ')
print('etc.')
