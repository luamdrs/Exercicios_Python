valor_casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Anos de financiamento: '))
# O valor da prestação será a quantidade de anos que deseja financiar multiplicado por 12 meses e dividido pelo valor da casa.
prestacao = valor_casa / (anos * 12)
minimo = salario * 30 / 100
print(f'Para pagar uma casa de R${valor_casa:.2f} em {anos} anos, a prestação será no valor de R${prestacao:.2f}')
# A prestação mensal não pode exceder 30% do salário do comprador.
if prestacao <= minimo:
    print('Empréstimo pode ser \033[1;32mCONCEDIDO\033[m!')
else:
    print('Empréstimo \033[1;31mNEGADO\033[m!')