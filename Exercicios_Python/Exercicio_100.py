from random import randint
from time import sleep


def sorteia(lista):
    print('=-' * 40)
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.4)


def soma_par(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'\nSomando os valores pares da lista {lista}, temos um total de: {soma}')
    print('=-' * 40)


numero = list()
sorteia(numero)
soma_par(numero)
