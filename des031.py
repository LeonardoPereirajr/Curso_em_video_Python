viagem = float(input('Quantos Km tem sua viagem ? : '))
if viagem>=200:
    custo = (viagem*0.45)
    print('Sua viagem de {} km custará R$ {:.2f}'.format(viagem, custo))
else:
    custo =(viagem*0.50)
    print('Sua viagem de {} km custará R$ {:.2f}'.format(viagem, custo))