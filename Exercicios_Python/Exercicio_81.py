# Valores em ordem decrescente em uma lista
lista = list()
cont = 0
print('=-' * 20)
while True:
    numero = int(input('Digite um valor: '))
    lista.append(numero)
    cont += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Desejar continuar [S/N]? ')).strip().upper()
    if continuar == 'N':
        break

print('=-' * 20)
print(f'Você digitou {cont} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {lista}')
if 5 in lista:
    print('O valor 5 faz parte da sua lista.')
else:
    print('O valor 5 não faz parte da sua lista.')
print('=-' * 20)
