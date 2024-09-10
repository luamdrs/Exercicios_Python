# Sorteio de Valores aleatórios (número maior e menor)
from random import randint

print('=-' * 25)
numeros = randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)
print('Os números sorteados foram: ', end='')
for num in numeros:
    print(num, end=' ')

print(f'\nO maior número é: {max(numeros)}')
print(f'O menor número é: {min(numeros)}')
print('=-' * 25)
