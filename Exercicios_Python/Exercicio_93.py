jogador = dict()
partidas = list()

jogador['Nome do Jogador'] = str(input('Nome do jogador: '))
cont_partidas = int(input(f'Quantas partidas {jogador["Nome do Jogador"]} jogou? '))

for c in range(1, cont_partidas + 1):
    # Adiciona a quantidade de gols na lista 'partidas'.
    partidas.append(int(input(f'   => Quantos gols na partida {c}? ')))
    
jogador['Gols'] = partidas[:] # A nova chave 'Gols' recebe uma cópia da lista 'partidas'.
jogador['Total'] = sum(partidas) # A nova chave 'Total' recebe a soma dos gols feitos nas 'partidas'.

print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)

print(f'O jogador {jogador['Nome do Jogador']} jogou {len(jogador['Gols'])} partidas.')

for i, v in enumerate(jogador['Gols']):
    print(f'   => Na partida {i + 1}, fez {v} gols.')

print(f'Foi um total de {jogador["Total"]} gols.')