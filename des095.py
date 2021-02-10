time = []
jogador={}
partidas=[]
while True:
    jogador.clear()
    jogador['Nome'] = str(input(' Nome do Jogador : '))
    tot = int(input(f' Quantas partidas {jogador["Nome"]} jogou ?: '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input('Quantos gols na partida ? : ')))
    jogador['gols'] = partidas[:]
    jogador['total'] =sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input(' Quer continuar ?')).upper()[0]
        if resp in 'SN':
            break
        print(' ERRO responda S ou N.')
    if resp == 'N':
        break
print('=+'*30)
print('cod  ', end='')
##CABEÇALHO
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
## VISUALIZAÇÃO DE DADOS
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('=+'*30)
## DADOD POR JOGADOR
while True:
    busca = int(input(' Mostrar dados de qual jogador ?[999 para parar] '))
    if busca == 999:
        break
    if busca>= len(time):
        print(f' ERRO! Não existe jogador com este codigo {busca}!')
    else:
        print(f' ---LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]} : ' )
        for i, g in enumerate(time[busca]['gols']):
            print(f'    NO jogo {i+1} fez {g} gols')
