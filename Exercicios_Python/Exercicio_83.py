# Verificador de expressão
expressao = str(input('Digite a expressão: '))
pilha = []
for simbolo in expressao:      # Para cada simbolo dentro da expressão,
    if simbolo == '(':         # se o usuário digitar '('
        pilha.append('(')      # então esse símbolo será adicionado à pilha.
    elif simbolo == ')':       # Se o usuário digitar ')', eu vou ter duas possibilidades:
        if len(pilha) > 0:     # Se a pilha estiver cheia, ou seja, se o tamanho dela for maior que 0,
            pilha.pop()        # O último elemento da pilha será excluído
        else:                  # Caso contrário, a pilha estará vazia
            pilha.append(')')  # e isso significa que teve mais parênteses fechando do que abrindo.
            break              # e então o programa para.
if len(pilha) == 0:            # Cada parêntese que abriu, teve sua relação com o parêntese fechando.
    print('Sua expressão é válida!')
else:                          # Se o tamanho da pilha for maior que zero.
    print('Sua expressão está errada!')