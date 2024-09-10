# Lista composta e análise de dados
lista1 = list()
lista_atualizada = list()
maior = menor = 0
print('=-' * 20)

while True:
    lista1.append(str(input('Nome: ')).strip().upper())
    lista1.append(float(input('Peso: ')))
    lista_atualizada.append(lista1[:])
    lista1.clear()

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if continuar in 'N':
        break

for indice, info in enumerate(lista_atualizada):
    if indice == 0:
        maior = menor = info[1]
    else:
        if info[1] > maior:
            maior = info[1]
        if info[1] < menor:
            menor = info[1]
print('=-' * 20)
print(f'Ao todo, há {len(lista_atualizada)} pessoas registradas.')
print(f'O maior peso foi {maior}kg. Peso de:', end=' ')
for p in lista_atualizada:
    if p[1] == maior:
        print(f'[{p[0]}]')
print(f'O menor peso foi {menor}kg. Peso de:', end=' ')
for p in lista_atualizada:
    if p[1] == menor:
        print(f'[{p[0]}]')
print('=-' * 20)
