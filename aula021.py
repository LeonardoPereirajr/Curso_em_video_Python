def contador(i,f,p):
    """
        FAZ UMA CONTAGEM
        :param i: INICIO
        :param f: FIM
        :param p: PASSO DA CONTAGEM
        :return: SEM RETORNO
    """
    c=i
    while c<=f:
        print(f'{c} ', end='')
        c+=p
    print('FIM')

help(contador)
