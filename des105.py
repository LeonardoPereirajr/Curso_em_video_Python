def notas(*n, sit=False):
    """
    -> FUNÇAO PARA ANALISAR NOTAS E SITUAÇÕES DOS ALUNOS
    :param n: uma ou mais notas dos alunos
    :param sit: indica se deve ou nao mostrar a situação do aluno
    :return: dicionario com varias informaçoes sobre o aluno
    """

    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'boa'
        elif r['media'] >= 5:
            r['situação'] = 'razoavel'
        else:
            r['situação'] ='ruim'
    return r

resp = notas(5.5, 9, 2.5,8.5,sit=True)
print(resp)
help(notas)
