print('=-' * 20)
numero = int(input('Digite um número para ver sua tabuada: '))
print('=-' * 20)
for i in range(1, 11):
    total = numero * i
    print(f'{numero} x {i} = \033[1;36m{total}\033[m')
print('=-' * 20)