# Valores em ordem crescente em uma lista
valores = list()
print('=-' * 20)

while True:
    numero = int(input('Digite um valor: '))
    if numero not in valores:
        valores.append(numero)
        print(f'O número {numero} foi adicionado com sucesso!')
    else:
        print(f'Não foi possível adicionar o número {numero}. '
              f'Esse número já faz parte da sua lista. Tente outro número!')
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()
        print('=-' * 20)
    if continuar == 'N':
        break

valores.sort()
print(f'Os valores digitados foram: {valores}')
