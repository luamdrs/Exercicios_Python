from time import sleep
# Definindo as cores do programa (5º passo)
cores = (
    '\033[m',        # 0 - Sem cor
    '\033[0;30;45m', # 1 - Rosa
    '\033[7;30;45m', # 2 - Preto e Rosa
    '\033[7;30;44m', # 3 - Preto e Roxo
)


# Definindo a função 'ajuda' (2º passo)
def ajuda(com):
    # Chamamos a função 'título'
    titulo(f'Acessando o manual do comando \'{com}\'', 1)
    # Cor fixa (branco)
    print(cores[2], end='')
    help(com)
    print(cores[0], end='')
    sleep(2)


# Definindo a função 'título' (3º passo)
def titulo(msg, cor=0): # Se o usuário não digitar nada, a cor padrão será zero
    # Essa função irá personalizar os '=-' de acordo com o tamanho do título
    tamanho = len(msg) + 4
    print(cores[cor], end='')
    print('=' * tamanho)
    print(f'  {msg}')
    print('=' * tamanho)
    print(cores[0], end='') # cores na posição zero (sem cor) para limpar a cor
    sleep(2)


# Programa Principal (1º passo)
comando = ''  # Variável str começará vazio
# Criamos um loop infinito para verificarmos uma função ou biblioteca. Caso a entrada do usuário seja a palavra 'Fim', o programa será finalizado. Caso contrário, o comando 'ajuda' será executado!
# Acrescentamos o título no programa principal (4º passo)
titulo('SISTEMA DE AJUDA PyHELP', 3)
while True:
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        titulo('FIM DO PROGRAMA. ATÉ LOGO! *-*', 1)
        break
    else:
        ajuda(comando)