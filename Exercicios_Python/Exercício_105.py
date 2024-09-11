def notas(*n, sit=False):
    """
    ~> Função para analisar notas e situações de alunos
    :param n: Múltiplas notas (uma ou mais)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação (True ou False)
    :return: Dicionário com várias informações sobre a situação dos alunos
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'
    return r


resp = notas(6, 7.5, 9, 10, 10, sit=True)
print(resp)
help(notas)
