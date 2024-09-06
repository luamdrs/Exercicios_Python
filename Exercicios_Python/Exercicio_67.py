# Tabuada com qualquer número, exceto negativos.
while True:
    print('*-' * 25)
    numero = int(input('Digite um número para calcularmos sua tabuada: '))
    print('*-' * 25)

    if numero < 0:
        break
    for n in range(1, 11):
        print(f'{numero} x {n} = {numero * n}')
print('Programa encerrado! Volte sempre! =)')