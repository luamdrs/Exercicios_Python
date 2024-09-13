# Função de porcentagem(aumentar)
def aumentar(preco=0, taxa=0, formato=False):
    valor = preco + (preco * taxa / 100)
    '''Retorna o valor com ponto, ao invés de vírgula caso o formato seja Falso. Caso seja Verdadeiro, retorna o valor formatado 'moeda(valor)'''
    return valor if formato is False else moeda(valor)


# Função de porcentagem(diminuir)
def diminuir(preco=0, taxa=0, formato=False):
    valor = preco - (preco * taxa / 100)
    return valor if formato is False else moeda(valor)


# Função de dobro
def dobro(preco=0, formato=False):
    valor = preco * 2
    return valor if formato is False else moeda(valor)


# Função de metade
def metade(preco=0, formato=False):
    valor = preco / 2
    return valor if formato is False else moeda(valor)


# Função de formatação de moeda
def moeda(preco=0, moed='R$'):
    return f'{moed}{preco:.2f}'.replace('.', ',')


# Função resumo (taxa aumento e redução)
def resumo(preco=0, taxa_aum=10, taxa_red=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'Com {taxa_aum}% de aumento: \t{aumentar(preco, taxa_aum, True)}')
    print(f'Com {taxa_red}% de redução: \t{diminuir(preco, taxa_red, True)}')
    print('-' * 30)