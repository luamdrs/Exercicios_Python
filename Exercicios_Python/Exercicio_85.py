lista = [[], []]
numero = 0

print('~' * 25)
for cont in range(1, 8):
    numero = int(input(f'Digite o {cont}º valor: '))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)
print('~' * 25)

lista[0].sort()
print(f'Números pares: {lista[0]}')
lista[1].sort()
print(f'Números ímpares: {lista[1]}')
