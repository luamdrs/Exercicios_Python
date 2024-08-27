# Procurando uma String dentro de outra
nome = str(input('Digite seu nome completo: ')).strip().upper()
print(f'Seu nome tem "Silva"? {'SILVA' in nome}')