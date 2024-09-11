numero = 0
soma = 0
cont = 0
numero = int(input('Digite um número [999 para parar]: '))  # Um input fora do loop para o 999 não ser contado na soma e nem na contagem
while numero != 999:
    soma += numero
    cont += 1
    numero = int(input('Digite um número [999 para parar]: '))
print(f'{cont} números foram digitados e a soma deles é igual a {soma}.')