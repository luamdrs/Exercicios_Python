# Converte a frase em letras maiúsculas e sem espaços
frase = str(input('Digite uma frase: ')).upper().strip() 
palavras = frase.split()  # Gera uma lista com as palavras
junto = ''.join(palavras)   # Junção da lista(frase) em uma única string 
frase_invertida = ''
for letra in range(len(junto) - 1, -1, -1):  # Vai da última letra até a primeira, voltando uma letra.
    frase_invertida += junto[letra]
print(f'O inverso de {junto} é \033[1;35m{frase_invertida}\033[m.')
if frase_invertida == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada NÃO É um palíndromo!')