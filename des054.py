from datetime import date
ano = date.today().year
cont_menor = 0
cont_maior= 0
for c in range(1,8):
    pes1 = int(input('Em que ano a {} a Pessoa nasceu : '.format(c)))
    if ano-pes1>=21:
        cont_maior+=1
    else:
        cont_menor+=1
print('Neste Grupo ao todo tivemos {} maiores de idade.'.format(cont_maior))
print('Tivemos {} pessoas menores de idade.'.format(cont_menor))