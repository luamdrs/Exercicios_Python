from datetime import date

ano_nascimento = int(input('Ano de Nascimento: '))
data_atual = date.today().year
idade = data_atual - ano_nascimento

print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')