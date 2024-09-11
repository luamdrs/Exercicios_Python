def escreva(msg):
    tamanho = len(msg) + 4
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)


frase = str(input('=> Digite uma frase: '))
escreva(frase)