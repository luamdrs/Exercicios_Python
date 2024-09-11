from datetime import date

ano = int(input('Qual o ano que você deseja analisar? [Digite 0 para analisar o ano atual] '))
if ano == 0:
    ano = date.today().year # Usamos essa função para sabermos a data atual.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO.')
else:
    print(f'O ano {ano} NÃO É BISSEXTO.')
