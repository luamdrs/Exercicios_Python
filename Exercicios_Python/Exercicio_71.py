# SIMULADOR CAIXA ELETRÔNICO
print('=' * 40)
print('{:^40}'.format(' BANCO CeV '))
print('=' * 40)
valor = int(input('Qual o valor que você deseja sacar? R$'))
# Valor total (montante) e esse total vai começar com o valor inteiro (que preciso sacar)
total = valor
# Declara a maior cédula que o caixa oferece
cedula = 50
# Total de cédulas vai começar com 0 porque não sabemos qual o valor exato
total_celulas = 0
# O loop vai ocorrer enquanto o valor não acabar (o dinheiro)
while True:
    if total >= cedula:     # Se o valor total que o usuario digitar for maior que o valor da cédula (50):
        total -= cedula     # então o total vai receber o valor total menos a cédula.
        total_celulas += 1  # Contagem pra saber quantas notas de 50 foram tiradas
    else:                   # Se não der para tirar os 50, iremos ver qual a cédula que será utilizada.
        if total_celulas > 0:
            print(f'Total de {total_celulas} cédulas de R${cedula}')
        # Se as cédulas de 50 acabarem, faz o mesmo processo com outras cédulas
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_celulas = 0  # E cada vez que a cédula é mudada, o total de cédulas retorna a 0
        # Se o dinheiro acabar, ou seja, se não estiver devendo mais nenhuma cédula, o programa acaba.
        if total == 0:
            break

print('=' * 40)
print('{:^40}'.format(' BANCO CeV AGRADECE! VOLTE SEMPRE! '))
print('=' * 40)
