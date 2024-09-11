from datetime import date
data_atual = date.today().year

cont_maior = cont_menor = 0
for posicao in range(1, 8):
    data_nascimento = int(input(f'Em que ano a {posicao}ª pessoa nasceu? '))
    idade = data_atual - data_nascimento
    if idade >= 18:
        cont_maior += 1
    else:
        cont_menor += 1
print(f'Ao todo tivemos {cont_maior} pessoas MAIORES de idade e {cont_menor} pessoas MENORES de idade. ')