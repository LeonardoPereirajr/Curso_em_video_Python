km = int(input('Quantos KM o carro percorreu ? : '))
dias = int(input('Quantos dias foi alugado o carro ? :'))
pagar = (dias * 60) + (km * 0.15)
print(' Voce rodou por {} dias o total de {} km e ir pagar R$ {:.2f}'.format(km,dias,pagar))