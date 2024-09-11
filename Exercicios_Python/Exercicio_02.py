nome = str(input('Digite seu nome completo: '))
idade = int(input('Qual é a sua idade? '))
print('Seu nome completo é: {}{}{}'.format('\033[1;35m', nome,'\033[m'))
print('Você tem {}{}{} anos.'.format('\033[1;34m', idade, '\033[m'))