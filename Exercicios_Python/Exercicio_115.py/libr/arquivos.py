# Função para verificar se o arquivo existe
from .interface import cabecalho


def arquivoExiste(nome):
    '''Iremos tentar abrir o arquivo com a função 'open' '''
    try:
        a = open(nome, 'rt')    # read text -> leitura de texto
        a.close()               # Fecha o arquivo
    except FileNotFoundError:   # Caso o arquivo não for encontrado, retorna Falso
        return False
    else:
        return True
    

# Função para criar o arquivo
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')  # write text: escreve um arquivo de texto, caso não exista
        a.close()              # Fecha o arquivo
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


# Função para ler o arquivo
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        cabecalho('\033[37mPESSOAS CADASTRADAS\033[m')
        '''Para cada linha dentro do arquivo, separa os arquivos por (;) e armazena na lista 'dados'. 
        Substitui a quebra de linha por um espaço entre nome e idade. 
        Imprime o nome e a idade [lista - indice 0 e 1]'''
        for linha in a:                              
            dados = linha.split(';')              
            dados[1] = dados[1].replace('\n', '')
            print(f'{dados[0]:<30}{dados[1]:>4} anos')
    finally:
        a.close()  # Fecha o arquivo (anyway)


# Função para cadastrar arquivo, nome e idade
def cadastrar(arquivo, nome='<Desconhecido>', idade=0):
    try:
        a = open(arquivo, 'at')  # append text: armazena o arquivo
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            '''Caso dê certo, escreve dentro do arquivo'''
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()  # Fecha o arquivo


# Função para remover uma pessoa do arquivo
def remover(arquivo, nome):
    try:
        # Lê os dados existentes
        with open(arquivo, 'rt') as a:
            linhas = a.readlines()
    except FileNotFoundError:
        print('Arquivo não encontrado!')
        return
    
    # Filtra as linhas que não contêm o nome a ser removido
    linhas_filtradas = [linha for linha in linhas if linha.split(';')[0] != nome]

    # Verifica se algo foi removido
    if len(linhas_filtradas) == len(linhas):
        print(f'Nenhum registro encontrado para {nome}.')
    else:
    # Reescreve o arquivo com as linhas filtradas
        with open(arquivo, 'wt') as a:
            a.writelines(linhas_filtradas)
        print(f'Registo de {nome} removido com sucesso!')
