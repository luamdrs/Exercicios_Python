velocidade = float(input('Qual é a velocidade do carro? '))
if velocidade > 80:
    print('MULTADO! 🚩\nVocê ultrapassou o limite permitido que é de até 80km/h.')
    multa = (velocidade - 80) * 7.00
    print('O valor da sua multa é de R${:.2f}.'.format(multa))
print('Tenha um bom dia e dirija com segurança!')