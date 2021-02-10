def voto(ano):
    from datetime import date
    print('-------------------------')
    ano_hoje = date.today().year
    cont = ano_hoje - ano
    if cont >= 60:
        return f' Com {cont} anos : VOTO OPCIONAL'
    elif cont < 16:
        return f' Com {cont} anos : VOTO NEGADO'
    else:
        return f' Com {cont} anos : VOTO OBRIGATORIO'


ano = int(input('Em que ano você nasceu ? :  '))
print(voto(ano))

