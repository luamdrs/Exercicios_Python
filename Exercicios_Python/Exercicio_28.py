# Jogo da Adivinhação
from random import randint
from time import sleep

print('-=-' * 20)
print('Eu irei pensar em um número entre 1 e 10. Tente adivinhar!')
print('-=-' * 20)
sleep(2)

player = int(input('Em qual número eu pensei? '))
robot = randint(1, 10)
print('PROCESSANDO...')
sleep(2)

if player != robot:
    print('Você errou! 🔴\nO número que você digitou foi {} e o número que eu pensei foi o {}.'.format(player, robot))
else:
    print('Você acertou! ⭐\nO número que você digitou foi {} e o número que eu pensei foi o {}.'.format(player, robot))
print('-=-' * 20)