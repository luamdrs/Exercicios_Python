from time import sleep


def maior(* num):
    cont = maior = 0
    print('=-' * 30)
    print('Analisando os valores passados...')

    for valor in num:
        print(f'[{valor}]', end='', flush=True)
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nAo todo, foram informados {cont} números.')
    sleep(0.5)
    print(f'O maior número informado foi {maior}.')
    sleep(0.5)


maior(2, 9, 4, 8, 6, 7)
maior(6, 7, 8, 10)
maior(5, 8, 1)
maior(7, 3)
maior(5)
maior()