import random
from time import sleep
lista = [0,1,2,3,4,5]
aleatorio = random.choice(lista)
print(20*'=')
print(" JOGO DA ADIVINHAÇÃO")
print(20*'=')
escolha = int(input("Digite um numero de 0 a 5: "))
print('PROCESSANDO...')
sleep(2)
while escolha != aleatorio:
    escolha = int(input("Voce errou. Tente novamente um numero de 0 a 5: "))
print('O numero era {} e você escolheu correto.'.format(aleatorio))
print(20*'=')