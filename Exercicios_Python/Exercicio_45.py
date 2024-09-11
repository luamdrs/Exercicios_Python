from random import randint
from time import sleep

opcoes = ('PEDRA', 'PAPEL', 'TESOURA')
print('=-' * 20, 'JOKENPO GAME', '=-' * 20)
print('''OPÇÕES:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

# Validação da entrada do jogador
while True:
    try:
        jogador = int(input('Digite a sua opção: '))
        if jogador in [0, 1, 2]:
            break
        print('Opção Inválida! Por favor, escolha 0, 1 ou 2.')
    except ValueError:
        print('Entrada Inválida! Por favor, insira um número inteiro: ')

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
computador = randint(0, 2)
print('-=' * 20)
print(f'Eu joguei {opcoes[computador]} e você jogou {opcoes[jogador]}.')
print('-=' * 20)

if computador == 0:
    if jogador == 0:
        print('Houve um empate aqui! Que tal tentarmos mais uma vez? 😏')
    elif jogador == 1:
        print('Você me venceu! Parabéns! ⭐')
    elif jogador == 2:
        print('Eu te venci hahahaha 😈')
elif computador == 1:
    if jogador == 0:
        print('Eu te venci hahahaha 😈')
    elif jogador == 1:
        print('Houve um empate aqui! Que tal tentarmos mais uma vez? 😏')
    elif jogador == 2:
        print('Você me venceu! Parabéns! ⭐')
elif computador == 2:
    if jogador == 0:
        print('Você me venceu! Parabéns! ⭐')
    elif jogador == 1:
        print('Eu te venci hahahaha 😈')
    elif jogador == 2:
        print('Houve um empate aqui! Que tal tentarmos mais uma vez? 😏')