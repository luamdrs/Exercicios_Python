# Gerador de PA
print('=-=-=-=-= Gerador de PA =-=-=-=-=')
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

termo = primeiro_termo
cont = 1

while cont <= 10:
    print(f'{termo}', end=' -> ')
    termo += razao
    cont += 1

print('FIM')