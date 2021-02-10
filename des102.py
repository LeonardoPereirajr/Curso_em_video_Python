def fatorial(num,show=False):
    """
    -> CALCULA O FATORIAL DE UM NUMERO
    :param num: o numero a ser calculado
    :param show: mostra ou nao calculo
    :return: retorna o resultado
    """
    f = 1
    for c in range(num,0, -1):
        if show :
           print(c, end='')
           if c > 1:
             print(' x ', end=' ')
           else:
             print(' = ', end=' ')
        f *= c
    return f


#main
n = int(input('Digite um numero : '))
print(fatorial(n,show=False))
help(fatorial)