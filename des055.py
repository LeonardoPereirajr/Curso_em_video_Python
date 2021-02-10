peso_maior = 0
peso_menor= 0
for p in range(1,6):
    peso = float(input('Qual o peso da {}a pessoa  : '.format(p)))
    if p==1:
        peso_maior = peso
        peso_menor = peso
    else:
        if peso>peso_maior:
            peso_maior=peso
        if peso<peso_menor:
            peso_menor=peso
print('Neste grupo o maior peso foi {} kg.'.format(peso_maior))
print('Neste grupo o menor peso foi {} kg.'.format(peso_menor))