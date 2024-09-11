def voto(ano):
    from datetime import date
    data_atual = date.today().year
    idade = data_atual - ano
    
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    elif 16 <= idade < 18 or idade >= 70:
        return f'Com {idade} anos: O VOTO É FACULTATIVO!'
    else:
        return f'Com {idade} anos: O VOTO É OBRIGATÓRIO!'
    

# Programa Principal
ano_nasc = int(input('Em que ano você nasceu? '))
print(voto(ano_nasc))