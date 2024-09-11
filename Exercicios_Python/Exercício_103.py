def ficha(jogador='<desconhecido>', gols=0):
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')

n = str(input('Nome do jogador: '))
g = str(input('Números de gols: '))

# 1º passo: Essa linha verifica se a entrada g é um valor numérico. O método isnumeric() retorna True se todos os caracteres na string forem dígitos.
# 2º passo: Se a entrada g for numérica, ela é convertida para um número inteiro e armazenada novamente na variável g.
# 3º passo: Se a entrada g não for numérica (por exemplo, se o usuário inseriu texto em vez de números), o programa define g como 0.
if g.isnumeric():
    g = int(g)
else:
    g = 0

# 1º passo: Verifica se o nome do jogador n está vazio. O método strip() remove espaços em branco no início e no fim da string, então essa verificação detecta se o usuário não inseriu nenhum nome.
# 2º passo: Se o nome do jogador estiver vazio, a função ficha é chamada com o argumento gols=g, usando o valor padrão '<desconhecido>' para o nome do jogador.
# 3º passo: Se o nome não estiver vazio, a função ficha é chamada com os argumentos n e g, usando os valores fornecidos pelo usuário.
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)