from time import sleep
from random import choice

print('=-' * 30)
print('Oi! Eu sou seu computador...')
sleep(2)
print('Acabei de pensar em um número entre 0 e 10.')
sleep(2)
print('Será que você consegue adivinhar qual foi?')
print('=-' * 30)
sleep(2)

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
computador = choice(lista)
acertou = False
palpite = 0

while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez!')
        elif jogador > computador:
            print('Menos... Tente mais uma vez!')
print('=-' * 30)
print(f'Você acertou com {palpite} tentativas. Parabéns! 🎉')
print('=-' * 30)