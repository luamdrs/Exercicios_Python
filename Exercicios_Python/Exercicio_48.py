soma = 0
cont = 0
# Encontrando os números ímpares de 1 a 500
for i in range(1, 501, 2):  
    if i % 3 == 0:  # Se o número for divisivel por 3
        soma += i   # A soma será igual a soma + o número (soma de todos os números divisíveis por 3)
        cont += 1   # E o contador será igual ao contador + 1 (vai contar quantos números % 3 há, de 1 em 1)
print(f'A soma de todos os {cont} valores é: {soma}')