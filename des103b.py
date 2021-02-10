def ficha(jog='<desconhecido>',gol=0):
    if jog== '':
        jog = 'desconhecido'
    if not gol.isnumeric():
        gol=0
    return f' O jogador {jog} fez {gol} gols(s) no campeonato'


n = str(input('Nome do jogador : ')).strip()
g = str(input('Numero de Gols : '))
print(ficha(n,g))