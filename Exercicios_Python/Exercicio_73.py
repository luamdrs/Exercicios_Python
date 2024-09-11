paises = ('Estados Unidos', 'China', 'Japão', 'Austrália', 'França', 'Holanda', 'Grã-Bretanha', 'Coréia do Sul', 'Itália', 'Alemanha', 'Nova Zelândia', 'Canadá', 'Uzbequistão', 'Hungria', 'Espanha', 'Suécia','Quênia', 'Noruega', 'Irlanda', 'Brasil')

print('=-' * 20)
print('QUADRO DE MEDALHAS DAS OLÍMPIADAS DE PARIS 2024')
print('=-' * 20)
print('20 PRIMEIRAS COLOCAÇÕES')
print('=-' * 20)

for pais in paises:
    print(pais)
print('=-' * 20)

print(f'Os 5 primeiros países colocados são: {paises[0:5]}')
print('=-' * 20)

print(f'Os 4 últimos países colocados são: {paises[16:]}')
print('=-' * 20)

print(f'PAÍSES EM ORDEM ALFABÉTICA: {sorted(paises)}')
print('=-' * 20)

print(f'O Brasil está na {paises.index('Brasil') + 1}ª colocação.')
print('=-' * 20)
