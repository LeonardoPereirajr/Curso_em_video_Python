import random
from time import sleep
lista = [0,1,2,3,4,5]
aleatorio = random.choice(lista)
print(20*'=')
print(" JOGO DA ADIVINHAÇÃO")
print(20*'=')
escolha = int(input("Digite um numero de 0 a 5: "))
print('PROCESSANDO...')
sleep(4)
if escolha == aleatorio:
    print('O numero era {} e você escolheu correto.'.format(aleatorio))
else:
    print('O numero era {} e você errou'.format(aleatorio))
print(20*'=')