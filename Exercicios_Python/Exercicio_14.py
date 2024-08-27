# Conversor de Temperaturas
c = float(input('Quantos ºC você deseja converter? '))
f = c * 9 / 5 + 32
print('{:.1f}ºC corresponde a {:.1f}ºF.'.format(c, f))