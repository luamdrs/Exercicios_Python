# Análise de Dados
soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_mais_velho = ''
menor_idade_mulher = 0

for p in range(1, 5):
    print(f'******** {p}ª PESSOA ********')
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip().upper()
    soma_idade += idade

# Verifica quem é o homem mais velho e o nome do homem
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome

# Verifica quantas mulheres tem menos de 20 anos
    if sexo in 'Ff' and idade < 20:
        menor_idade_mulher += 1

media_idade = soma_idade / 4
print(f'A média de idade de todas as pessoas do grupo é de {media_idade:.0f} anos.')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_mais_velho}.')
print(f'Ao todo, são {menor_idade_mulher} mulheres com menos de 20 anos.')