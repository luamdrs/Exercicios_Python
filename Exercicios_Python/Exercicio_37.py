numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[ 1 ] Conversão para BINÁRIO
[ 2 ] Conversão para OCTAL
[ 3 ] Conversão para HEXADECIMAL''')
opcao = int(input('Digite sua opção: '))
if opcao == 1:
    print(f'{numero} convertido para BINÁRIO é igual a: {bin(numero)[2:]}')
elif opcao == 2:
    print(f'{numero} convertido para OCTAL é: {oct(numero)[2:]}')
elif opcao == 3:
    print(f'{numero} convertido para HEXADECIMAL é: {hex(numero)[2:]}')
else:
    print('Opção INVÁLIDA. Tente novamente!')