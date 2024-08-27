# Reajuste Salarial
salario1 = float(input('Salário do funcionário: R$'))
salario2 = (salario1 * 20 / 100) + salario1
print('O antigo salário do funcionário era R${:.2f}. Com um aumento de 20% ele passou a receber R${:.2f}.'.format(salario1, salario2))