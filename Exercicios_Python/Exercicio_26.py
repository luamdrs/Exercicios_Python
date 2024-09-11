frase = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra A aparece quantas vezes na frase? {frase.count('A')}')
print(f'A primeira letra A aparece em qual posição? {frase.find('A') + 1}')
print(f'A última letra A aparece em qual posição? {frase.rfind('A') + 1}')