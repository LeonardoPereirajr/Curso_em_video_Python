velocidade = int(input('Qual a velocidade do carro? : '))
if velocidade>80:
    multa = (velocidade-80)*7
    print('Voce passou da velocidade permitida, sua multa é de R$ {}'.format(multa))
else:
    print('Voce é um bom motorista')
