# Análise de dados em uma Tupla
print('=-' * 20)
numero = (int(input('Digite o primeiro número: ')),
          int(input('Digite o segundo número: ')),
          int(input('Digite o terceiro número: ')),
          int(input('Digite o quarto número: ')))

print('=-' * 20)
print(f'Você digitou os valores: {numero}')
print('=-' * 20)
print(f'O número 2 apareceu {numero.count(2)} vezes.')
print('=-' * 20)

if 3 in numero:
    print(f'O valor 3 apareceu na {numero.index(3) + 1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')

print('=-' * 20)
print('Números pares: ', end='')
for valor in numero:
    if valor % 2 == 0:
        print(valor, end=' ')
