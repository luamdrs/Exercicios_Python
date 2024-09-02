# Validação de Dados
sexo_fem = 'F'
sexo_masc = 'M'
sexo = str(input('Informe o seu sexo [F/M]: ')).strip().upper()

while sexo != sexo_masc and sexo != sexo_fem:
    sexo = str(input('Dados inválidos! Informe o sexo corretamente: ')).strip().upper()

if sexo == 'F':
    sexo_fem = sexo
    print(f'O sexo {sexo_fem} foi registrado com sucesso!')
elif sexo == 'M':
    sexo_masc = sexo
    print(f'O sexo {sexo_masc} foi registrado com sucesso!')