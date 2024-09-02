# Calculando Fatorial com while

numero = int(input('Digite um número para calcular seu fatorial: '))
print(f'Calculando {numero}! = ', end=' ')
cont = numero  # O contador vai começar a partir do número que o usuário digitar
fatorial = 1

# Loop: enquanto o contador for maior que 0, o loop será executado
while cont > 0:
    print(f'{cont}', end=' ')
    print(' x ' if cont > 1 else ' = ', end=' ')  # se o cont for maior que 1, escreve x, se for menor, escreve =
    fatorial *= cont  # multiplicação de todos os números
    cont -= 1  # cont vai diminuindo os números até chegar em 1

print(f'{fatorial}')