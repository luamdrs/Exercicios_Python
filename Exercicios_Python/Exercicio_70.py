total = cont_preco = menor_preco = contador = 0
mais_barato = ' '

while True:
    produto = str(input('Nome do Produto: ').strip().upper())
    preco = int(input('Preço: R$').strip())
    contador += 1
    total += preco

    if preco > 1000:
        cont_preco += 1

    if contador == 1 or preco < menor_preco:
        menor_preco = preco
        mais_barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]? ').strip().upper())
    if resp == 'N':
        break

print(f'O total da compra foi R${total:.2f}')
print(f'Temos {cont_preco} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi {mais_barato} que custa R${menor_preco:.2f}')