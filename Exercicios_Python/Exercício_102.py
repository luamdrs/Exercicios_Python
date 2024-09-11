def fatorial(n, show=False):
    """
    ~> Calcula o fatorial de um número
    :param n: O número que será calculado
    :param show: Mostrar ou não a conta completa (Opcional - True ou False)
    :return: O valor do Fatorial de um número n.
    
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print('x ', end='')
            else:
                print('= ', end='')
        f *= c
    return f

print('~' * 30)
# Se mudar o show para False, ele mostrará apenas o resultado
print(fatorial(n=5, show=True))
print('~' * 30)