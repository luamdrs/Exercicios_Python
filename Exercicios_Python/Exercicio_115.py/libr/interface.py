# Função para verificar se a entrada é um número inteiro
def num_inteiro(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mErro: Por favor, digitar um número inteiro válido!\033[m')
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não informar os dados!\033[m')
            return 0
        else:
            return n


# Função para criar uma linha de separação
def linha(tam=40):
    return '-' * tam


# Função para exibir um cabeçalho de texto
def cabecalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())


# Função para criar um menu interativo
def menu(lista):
    cabecalho('\033[37mMENU PRINCIPAL\033[m')
    c = 1
    for item in lista:
        print(f'\033[37m[{c}]\033[m \033[36m{item}\033[m')
        c += 1 
    print(linha())
    opcao = num_inteiro('\033[37mSua opção: \033[m')
    return opcao
