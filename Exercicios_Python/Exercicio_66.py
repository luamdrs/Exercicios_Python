numero = cont = soma = 0
while True:
    numero = int(input('Digite um número [999 para parar]: '))
    if numero == 999:
        break
    soma += numero
    cont += 1
print(f'{cont} números foram digitados e soma de todos eles é: {soma}')