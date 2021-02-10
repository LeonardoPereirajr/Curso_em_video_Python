import random
from time import sleep
from operator import itemgetter
print('=+'*30)
print('                JOGO DE DADOS         ')
print('=+'*30)
jogadores={}
print('Valores Sorteados :')
jogadores = {'jogador1': random.randint(1, 6),
             'jogador2': random.randint(1, 6),
             'jogador3': random.randint(1, 6),
             'jogador4': random.randint(1, 6)}
for k, v in jogadores.items():
        print(f' O {k} tirou {v} no dado .')
        sleep(1)
print('=+'*30)
rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)## ORDENAR A PARTIR DA POSIÇÃO 1 POIS A POSIÇÃO 0 SÃO AS KEYS
print('=+'*30)
print('                RANKING         ')
for i, v in enumerate(rank):
    print(f'{i+1} º lugar: {v[0]} com {v[1]}.')
    sleep(1)
