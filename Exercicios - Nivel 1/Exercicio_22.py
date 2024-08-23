# Analisador de textos
frase = str(input('Digite uma frase: ')).strip()
print('Analisando sua frase...')
print(f'Sua frase com letras maiúsculas fica: {frase.upper()}')
print(f'Sua frase com letras minúsculas fica: {frase.lower()}')
print(f'Sua frase tem {len(frase) - frase.count(' ')} letras')
separar = frase.split()
print(f'A primeira palavra da sua frase é {separar[0]} e ela tem {len(separar[0])} letras.')