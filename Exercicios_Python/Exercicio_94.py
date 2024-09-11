grupo = list()
pessoa = dict()
soma = media = 0

while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo [M/F]: ')).upper().strip()
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    grupo.append(pessoa.copy())
    while True:
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()
        if continuar in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if continuar == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(grupo)} pessoas cadastradas.')
media = soma / len(grupo)
print(f'B) A média de idade é de {media} anos.')
print('C) As mulheres cadastradas foram: ', end='')
for p in grupo:
    if p['Sexo'] == 'F':
        print(f'{[p['Nome']]} ', end='')
print()
print(f'D) Lista das pessoas que estão acima da média: ', end='')
for p in grupo:
    if p['Idade'] > media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
print()
print('<< Programa encerrado >>')