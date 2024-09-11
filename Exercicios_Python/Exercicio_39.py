from datetime import date

ano_atual = date.today().year
data_nascimento = int(input('Ano de nascimento: '))
print('''Qual é o seu gênero? 
[ 1 ] Masculino
[ 2 ] Feminino''')
num = int(input('Digite uma opção: '))
if num == 1:
    print('\033[1;32mO alistamento para o gênero MASCULINO é obrigatório.\033[m')
elif num == 2:
    print('\033[1;31mO alistamento para o gênero FEMININO não é obrigatório!\033[m')
    exit()
else:
    print('\033[1;31mERROR. Tente novamente!\033[m')
    exit()

idade = ano_atual - data_nascimento
print(f'Quem nasceu em {data_nascimento} tem {idade} anos em {ano_atual}.')
if idade == 18:
    print('Você precisa se alistar IMEDIATAMENTE!')
elif idade < 18:
    # Para saber quantos anos ainda faltam para o alistamento
    resto = 18 - idade
    ano = ano_atual + resto
    print(f'Ainda faltam {resto} ano(s) para o alistamento.')
    print(f'Seu alistamento será em {ano}.')
elif idade > 18:
    # Para saber quantos anos se passaram do alistamento
    resto = idade - 18
    ano = ano_atual - resto
    print(f'Você deveria ter se alistado há {resto} anos(s).')
    print(f'Seu alistamento foi em {ano}.')