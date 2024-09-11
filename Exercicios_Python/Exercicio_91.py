# Jogos de Dados com Python
from random import randint
from operator import itemgetter
from time import sleep

ficha = dict()

ficha['Jogador 1'] = randint(1, 6)
ficha['Jogador 2'] = randint(1, 6)
ficha['Jogador 3'] = randint(1, 6)
ficha['Jogador 4'] = randint(1, 6)

ranking = list()

print('Valores sorteados:')
for i, jogador in ficha.items():
    print(f'{i} tirou {jogador} no dado.', )
    sleep(1)

print('=-' * 30)

ranking = sorted(ficha.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]} pontos.')

print('=-' * 30)