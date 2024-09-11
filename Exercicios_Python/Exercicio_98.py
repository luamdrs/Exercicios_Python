from time import sleep


def contador(i, f, p):
    # Convertendo número negativo em positivo.
    if p < 0:
        p *= -1
    # ERRO se o passo for igual a 0.
    if p == 0:
        print('Erro! 0 é um número inválido para essa posição!')
        quit()

    print('=-' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(2)

    # Teste para verificar quando o início for menor que o fim
    if i < f:
        cont = i
        while cont <= f:
            sleep(0.3)
            print(f'{cont} ', end=' ', flush=True)
            cont += p
        print('~ Fim!🏁')
    # Teste para verificar quando o início for maior ou igual ao fim
    else:
        cont = i
        while cont >= f:
            sleep(0.3)
            print(f'{cont} ', end=' ', flush=True)
            cont -= p
        print('~ Fim!🏁')


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('=-' * 20)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
