def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digitar um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            quit()
        else:
            return num


def leiaReal(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digitar um número real válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            quit()
        else:
            return num


n_int = leiaInt('Digite um número inteiro: ')
n_real = leiaReal('Digite um número real: ')
print(f'O valor inteiro foi {n_int} e o valor real foi {n_real}')
