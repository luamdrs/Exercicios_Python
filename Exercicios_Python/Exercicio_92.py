from datetime import datetime

dados = dict()

while True:
    dados['Nome'] = str(input('Nome: '))
    nasc = int(input('Ano de Nascimento: '))
    dados['Idade'] = datetime.now().year - nasc
    dados['Carteira de Trabalho'] = int(input('Carteira de Trabalho [0 não possui]: '))
    if dados['Carteira de Trabalho'] != 0:
        dados['Ano de Contratação'] = int(input('Ano de Contratação: '))
        dados['Salário'] = float(input('Salário: R$'))
        dados['Aposentadoria'] = dados['Idade'] + ((dados['Ano de Contratação'] + 35) - datetime.now().year) # O ano em que vai se aposentar - o ano atual
        print('=-' * 30)
        for i, v in dados.items():
            print(f'{i} = {v}')
        break
    elif dados['Carteira de Trabalho'] == 0:
        print('=-' * 30)
        for i, v in dados.items():
            print(f'{i} = {v}')
        break
print('=-' * 30)