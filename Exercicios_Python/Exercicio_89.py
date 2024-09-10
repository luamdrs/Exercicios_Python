# Boletim com listas compostas
from time import sleep

ficha = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if continuar == 'N':
        break
    
print('-=' * 30)
print(f'{'Nº.':<4}{'NOME':<9}{'MÉDIA':>8}')
print('-' * 26)

for i, aluno in enumerate(ficha):
    print(f'{i:<4}{aluno[0]:<9}{aluno[2]:>8.1f}')
while True:
    print('-' * 35)
    opcao = int(input('Você deseja verificar as notas de qual aluno? [Digite 999 para finalizar o programa] '))
    if opcao == 999:
        print('Finalizando o programa...')
        sleep(1)
        break
    if opcao <= len(ficha) - 1:
        print(f'As notas de {ficha[opcao][0]} são: {ficha[opcao][1]}')
print('*-* Volte sempre! *-*')