# Aumento de 10% e 15% no salário do funcionário
salario = float(input('Digite o salário do funcionário: R$'))
if salario > 1250:
    novo_salario = (salario * 10 / 100) + salario
else:
    novo_salario = (salario * 15 / 100) + salario
print(f'Quem ganhava R${salario:.2f}, agora passa a receber R${novo_salario:.2f}')