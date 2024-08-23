# Primeiro e último nome de uma pessoa
nome = str(input('Digite seu nome completo: ')).strip().title()
separar = nome.split()
print(f'Prazer em te conhecer, {nome}.')
print(f'Seu primeiro nome é: {separar[0]}')
print(f'Seu último nome é: {separar[len(separar) - 1]}')
