from math import hypot
a = float(input('Cateto Oposto: '))
b = float(input('Cateto Adjacente: '))
h = hypot(a, b)
print('A hipotenusa é: {:.2f}'.format(h))