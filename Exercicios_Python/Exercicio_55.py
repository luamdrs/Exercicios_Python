maior_peso = 0
menor_peso = 0

# Criando o prompt para o usuário (1 a 5)
for p in range(1, 6):
    peso = float(input(f'Qual é o peso da {p}ª pessoa? '))
    if p == 1:  # Leu o peso da primeira pessoa
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso: 
            maior_peso = peso  
        if peso < menor_peso:
            menor_peso = peso
print(f'O maior peso lido foi de: {maior_peso}kg'
      f'\nO menor peso lido foi de: {menor_peso}kg')