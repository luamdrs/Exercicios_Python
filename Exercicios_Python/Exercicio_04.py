# Dissecando uma variável
x = input('Digite algo: ')
print('Tipo primitivo: ', type(x))
print('Só tem espaços? ', x.isspace())
print('É um número? ', x.isnumeric())
print('É alfabético? ', x.isalpha())
print('É alfanumérico? ', x.isalnum())
print('Tem apenas letras maiúsculas? ', x.isupper())
print('Tem apenas letras minúsculas? ', x.islower())
print('Ela está capitalizada? ', x.istitle())