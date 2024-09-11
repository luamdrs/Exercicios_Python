primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

termo = primeiro
cont = 1
total = 0  # total de termos que o usuário vai digitar
mais = 10  # a quantidade que o programa começa a mostrar (10 números)

# Se o usuário digitar um numero diferente de 0, o loop acontece. Caso contrário, ele é finalizado.
while mais != 0:
    total += mais  # O total vai ser o total que ele vai querer + os 10 números já mostrados
    while cont <= total:
        print(f'{termo}', end=' ~> ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? [Digite 0 para parar] '))

print(f'A progressão foi finalizada com {total} termos mostrados.')