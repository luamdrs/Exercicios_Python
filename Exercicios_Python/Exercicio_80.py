# Lista ordenada sem repetições
lista = list()

for c in range(0, 5):
    numero = int(input('Digite um valor: '))
    # Verificação do primeiro número.
    if c == 0:
        lista.append(numero)
        print('Número adicionado ao final da lista!')
    # Verifico se o número digitado é maior que o número que está no último elemento lista[len(lista)-1] ou lista[-1].
    elif numero > lista[-1]:
        lista.append(numero)
    # Irei verificar dentro de cada posição se o número que eu quero inserir é menor ou igual a ele. Se ele for menor ou igual, vou inserir o valor em uma posição específica sem precisar usar o append.
    else:
        pos = 0
        # Vai da posição 0 até a última posição.
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                print(f'Número adicionado na {pos}ª posição.')
                # break porque só vai acontecer uma vez.
                break
            # Vai passando de posição em posição.
            pos += 1
print(f'Os valores digitados em ordem foram: {lista}')
