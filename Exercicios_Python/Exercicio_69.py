print('=-' * 20)
print('        CADASTRE UMA PESSOA')
print('=-' * 20)

maior_18anos = menor_20anos = homens = 0

while True:
    idade = int(input('Idade: ').strip())
    if idade >= 18:
        maior_18anos += 1

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ').strip().upper())
    if sexo == 'M':
        homens += 1
    if sexo == 'F':
        if idade < 20:
            menor_20anos += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]? ').strip().upper())
    if continuar == 'S':
        print('=-' * 20)
        print('        CADASTRE UMA PESSOA')
        print('=-' * 20)
    if continuar == 'N':
        break

print('=-' * 20)
print(f'Total de pessoas maiores de 18 anos: {maior_18anos}')
print(f'Homens cadastrado(s): {homens}')
print(f'Mulheres com menos de 20 anos: {menor_20anos}')
print('=-' * 20)
