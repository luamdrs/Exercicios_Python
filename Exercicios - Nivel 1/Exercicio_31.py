# Condicional simplificada: If e Else na mesma linha
distancia = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a iniciar uma viagem de {distancia}km.')
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'E o preço da sua passagem será de R${preco:.2f}')