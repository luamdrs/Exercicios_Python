from time import sleep

print('Olá! Seja bem-vindo ao nosso programa! :)')
sleep(2)
opcao = 0
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))


while opcao != 5:

    print('''Menu de Opções: 
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA ''')

    opcao = int(input('Qual é a sua opção [1-5]? '))

    if opcao == 1:
        print(f'A soma dos números {n1} e {n2} é igual a: {n1 + n2}.')
    elif opcao == 2:
        print(f'A multiplicação dos números {n1} e {n2} é igual a: {n1 * n2}.')
    elif opcao == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2}, o MAIOR número é: {n1}.')
        elif n2 > n1:
            print(f'Entre {n1} e {n2}, o MAIOR número é: {n2}.')
        elif n1 == n2:
            print('Não há um número MAIOR, pois eles são IGUAIS.')
    elif opcao == 4:
        print('Informe os novos números: ')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Saindo do programa...')
        sleep(2)
    else:
        print('Opção inválida! Tente novamente!')
print('~' * 40)
print('O programa foi finalizado! Volte sempre!')
print('~' * 40)