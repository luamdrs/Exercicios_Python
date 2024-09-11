def leiaInt(msg):
    resolvido = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            resolvido = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido!\033[m')
        
        if resolvido:
            break
    return valor

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')