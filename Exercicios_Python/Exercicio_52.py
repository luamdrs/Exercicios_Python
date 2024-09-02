# Contador de números primos
numero = int(input('Digite um número: '))
cont = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        print('\033[1;32m', end='')
        cont += 1  
    else:
        print('\033[1;31m', end='')
    print(f'{i}', end=' ')
print(f'\n\033[mO número {numero} foi divisível {cont} vezes.')
# Para ser um número primo ele precisa ser divisível 2 vezes. Por 1 ou por ele mesmo.
if cont == 2: 
    print('Dessa forma, ele é PRIMO.')
else:
    print('Dessa forma, ele NÃO É PRIMO.')