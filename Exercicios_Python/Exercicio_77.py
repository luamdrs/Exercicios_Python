palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for p in palavras:
    print(f'\nNa palavra {p} temos as vogais: ', end=' ')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')
