valores = []
pares = []
impares = []
print('=-' * 20)

while True:
    numeros = valores.append(int(input('Digite um valor: ')))

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if resp == 'N':
        break

for indice, valor in enumerate(valores):
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
        
print('=-' * 20)
print(f'A lista completa é: {valores}')
print(f'Valores pares: {pares}')
print(f'Valores ímpares: {impares}')
print('=-' * 20)