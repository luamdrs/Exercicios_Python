# Contador de Números: Maior, Menor e Média utilizando o while
usuario = 'S'
soma = media = cont = maior = menor = 0
while usuario in 'Ss':
    numero = int(input('Digite um número: '))
    usuario = str(input('Quer continuar? [S/N] ')).upper().strip()
    soma += numero
    cont += 1
    # Passo para saber qual é o maior e o menor número
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
media = soma / cont
print(f'Você digitou {cont} número(s) e a média foi {media}.')
print(f'O maior número é {maior} e o menor é {menor}.')