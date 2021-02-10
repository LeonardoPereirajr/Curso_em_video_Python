jog={}
jogos={}
jog['Nome']=str(input(' Nome do Jogador : '))
jog['partidas'] = int(input(f' Quantas partidas {jog["Nome"]} jogou ?: '))
print(jog)
cont=0
gols=[]
cont_gols=0
total=0
n=0
while True:
       gols.append(int(input('Quantos gols na partida ? : ')))
       jog['gols'] = gols
       cont+=1
       total=sum(gols)
       if cont >= jog['partidas']:
           break
jog['total'] = total
print(jog)
print('=+'*30)
for k, v in jog.items():
        print(f'O campo {k} tem valor {v} ')
print('=+'*30)
print(f'O Jogador {jog["Nome"]} jogou {jog["partidas"]} partidas.')
for c in range(0,jog['partidas']) :
    print(f'Na partida {c+1} o jogador fez {jog["gols"][c]} gols')
print(f' Foi um total de {jog["total"]} gols')


