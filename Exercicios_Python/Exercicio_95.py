time = list()
partidas = list()
jogador = dict()

while True:
    # Apaga dados do jogador anterior antes de ler dados do próximo jogador.
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    qtd_partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    # Apaga dados anterior de 'partidas' antes de ler o próximo.
    partidas.clear()

    # Contador de gols em cada partida.
    # Acrescentamos cada gol na lista 'partidas' com o comando append
    for c in range(1, qtd_partidas + 1):
        partidas.append(int(input(f'   => Quantos gols na partida {c}? ')))
    # A nova chave 'Gols' recebe uma cópia da lista 'partidas'.
    jogador['Gols'] = partidas[:]
    # A nova chave 'Total' recebe a soma de todos os Gols.
    jogador['Total'] = sum(partidas)
    # A lista 'time' recebe uma cópia do dicionário 'jogador'.
    time.append(jogador.copy())

    # Loop infinito para questionar ao usuário se ele deseja continuar ou não.
    while True:
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()
        if continuar in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if continuar == 'N':
        break

# Cabeçalho
print('=-' * 30)
print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

# Dados/Resultados
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>2} ', end='')
    for dado in v.values():
        print(f'{str(dado):<15}', end='')
    print()
print('-' * 40)

# Qual é o jogador que você deseja ver os dados?
while True:
    busca = int(input('Mostrar dados de qual jogador [999 para parar]? '))
    if busca == 999:
        break
    if busca >= len(time):
        print('ERRO! Não existe jogador com o código informado.')
    # O nome do jogador ficará dentro da lista 'time' e dentro dessa lista, há um índice numérico com o nome 'busca' e dentro dele, temos o elemento 'Nome'.
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]['Nome']}:')
    # Levantamento de cada jogador de acordo a busca (cod digitado).
        for i, gol in enumerate(time[busca]['Gols']):
            print(f'   => No jogo {i + 1} fez {gol} gols.')
    print('-' * 40)
print('>> Fim do programa <<')