print('\033[1;36;40mDESAFIO 52 - AULA 13\033[m')
number = int(input('Coloque um número: '))
a = 0
for c in range(1, number + 1):
    if number % c == 0:
        a = a + 1
if a == 2:
    print("Esse número é primo!")
elif a != 2:
    print("Esse número não é primo!")
