preco1 = float(input('Preço antigo do produto: R$'))
preco2 = preco1 - (preco1 * 5 / 100)
print('O produto custava R${:.2f} e com um desconto de 5% o produto custará: R${:.2f}.'.format(preco1, preco2))