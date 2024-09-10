# Números em Extenso
numeros_extenso = ('zero', 'um', 'dois', 'três', 'quatro',
'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    numero = int(input('Digite um valor entre 0 e 20: '))
    if 0 <= numero <= 20:
        print(f'O valor que você digitou é -> {numeros_extenso[numero]}')

        while True:
            resp = input('Deseja continuar [S/N]? ').strip().upper()
            if resp in ('S', 'N'):
                break
            print('Resposta inválida! Por favor, digite S ou N.')

        if resp == 'N':
            print('Fim do programa')
            break
    else:
        print('Valor inválido! Digite um número entre 0 e 20.')