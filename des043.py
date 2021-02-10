peso = float(input('Qual seu peso ? : '))
altura = float(input('Qual sua altura ? : '))
imc = float(peso / (altura*altura))
if imc > 30 :
    print('Seu IMC é de {:.2f}'.format(imc))
    print('Obeso')
elif imc >25  :
    print('Seu IMC é de {:.2f}'.format(imc))
    print("Sobrepeso")
elif imc > 18:
    print('Seu IMC é de {:.2f}'.format(imc))
    print("Normal")
else:
    print('Seu IMC é de {:.2f}'.format(imc))
    print('Abaixo do peso')
