# Jogo do par ou ímpar
from random import randint

v = 0 
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P/I]? ')).strip().upper()
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}, ', end='')
    print('Deu PAR!' if total % 2 == 0 else 'Deu ÍMPAR!')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU! ')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAMER OVER! Você venceu {v} vezes.')