# Função de porcentagem
def aumentar(preco=0, taxa=0):
    valor = preco + (preco * taxa/100)
    return valor


# Função de dobro
def dobro(preco=0):
    valor = preco * 2
    return valor


# Função de metade
def metade(preco=0):
    valor = preco / 2
    return valor


# Função de formatação de moeda
def moeda(preco=0, moed='R$'):
    return f'{moed}{preco:.2f}'.replace('.', ',')
