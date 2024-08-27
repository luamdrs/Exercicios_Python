# Pintando a parede
largura = float(input('Largura: '))
altura = float(input('Altura: '))
area = largura * altura
litro = area / 2
print('Sua parede tem uma dimensão de {}x{} e a área corresponde a {}m².'.format(largura, altura, area))
print('Para pintar a sua parede, você precisará de {}L de tinta.'.format(litro))
