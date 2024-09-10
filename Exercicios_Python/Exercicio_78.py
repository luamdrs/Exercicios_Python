# Identificando maior e menor número em lista
numeros = list()
maior = menor = 0

print('=-' * 25)
for cont in range(0, 6):
    numeros.append(int(input(f'Digite um valor na {cont + 1}ª posição: ')))
    if cont == 0:
        maior = menor = numeros[cont]
    else:
        if numeros[cont] > maior:
            maior = numeros[cont]
        if numeros[cont] < menor:
            menor = numeros[cont]

print('-=' * 25)
print(f'Os valores digitados foram: {numeros}')
print('-=' * 25)

# Menor valor
print(f'O menor número digitado foi {menor} na posição: ', end='')
for indice, valor in enumerate(numeros):
    if valor == menor:
        print(f'{indice + 1}ª ', end='')
# Maior valor
print(f'\nO maior número digitado foi {maior} na posição: ', end='')
for indice, valor in enumerate(numeros):
    if valor == maior:
        print(f'{indice + 1}ª ', end='')