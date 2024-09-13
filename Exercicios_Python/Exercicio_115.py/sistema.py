from libr.arquivos import arquivoExiste, criarArquivo, lerArquivo, cadastrar, remover
from libr.interface import menu, cabecalho, num_inteiro
from time import sleep

arquivo = "cursoemvideo.txt"

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Remover pessoa', 'Sair do programa'])
    if resp == 1:
        # Opção de listar o conteúdo de um arquivo
        lerArquivo(arquivo)
    elif resp == 2:
        # Opção de cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = num_inteiro('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif resp == 3:
        cabecalho('REMOVER CADASTRO')
        nome = str(input('Nome da pessoa a remover: '))
        remover(arquivo, nome)
    elif resp == 4:
        cabecalho('\033[36mSaindo do sistema... Até logo!\033[m')
        sleep(1)
        break
    else:
        print('\033[31mERRO: Digite uma opção válida!\033[m')
    sleep(2)
