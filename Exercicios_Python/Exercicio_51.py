print('=-' * 20)
print('         10 TERMOS DE UMA PA')
print('=-' * 20)

primeiro_termo = int(input('Primeiro termo: '))  # Qual é o número inicial?
razao = int(input('Razão: '))  # Vai pular de quantos em quantos números?
decimo = primeiro_termo + (10 - 1) * razao  # fórmula do enésimo termo de uma PA
for cont in range(primeiro_termo, decimo + razao, razao):
    print(f'{cont}', end='➡️  ')
print('FIM')