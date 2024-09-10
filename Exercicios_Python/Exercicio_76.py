# Lista de Preços utilizando uma tupla
lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'Estojo', 25.99,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.30,
         'Canetas', 22.30,
         'Livro', 34.90)

print('-' * 40)
print(f'{'LISTA DE PREÇOS':^40}')
print('-' * 40)

soma = 0

for posicao in range(0, len(lista)):
    if posicao % 2 == 0:
        print(f'{lista[posicao]:.<30}', end=' ')
    else:
        print(f'R${lista[posicao]:>7.2f}')
        soma += lista[posicao]
print('-' * 40)
print(f'TOTAL {soma:>34.2f}')