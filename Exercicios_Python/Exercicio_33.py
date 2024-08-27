# Maior e Menor número
print('=-' * 20)
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))
print('=-' * 20)
# Verificação do menor número
menor_numero = numero1
if numero2 < numero1 and numero2 < numero3:
    menor_numero = numero2
if numero3 < numero1 and numero3 < numero2:
    menor_numero = numero3
# Verificação do maior número
maior_numero = numero1
if numero2 > numero1 and numero2 > numero3:
    maior_numero = numero2
if numero3 > numero1 and numero3 > numero2:
    maior_numero = numero3
print(f'O menor número é: {menor_numero}')
print(f'O maior número é: {maior_numero}')
print('=-' * 20)