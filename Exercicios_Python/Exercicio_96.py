def calculo(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} corresponde a {area}m².')


print('        Controle de Terrenos')
print('=-' * 20)
larg = float(input('Largura [m]: '))
comp = float(input('Comprimento [m]: '))
calculo(larg, comp)