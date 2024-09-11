dias = int(input('Dias de aluguel: '))
km = float(input('Km percorridos: '))
total = (60 * dias) + (0.15 * km)
print('O valor total pelo aluguel do carro será de R${:.2f}.'.format(total))