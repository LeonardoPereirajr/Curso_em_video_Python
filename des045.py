import random
from time import sleep
lista = [0,1,2]
aleatorio = random.choice(lista)
print(20*'=')
print(" JOGO DA ADIVINHAÇÃO")
print(20*'=')
print(" 0 = PEDRA")
print(" 1 = PAPEL")
print(" 2 = TESOURA")
escolha = int(input("Escolha Pedra, Papel ou Tesoura? : "))
print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PO...')
sleep(1)
if escolha == aleatorio:
    print('O jogador jogou {} e o computador jogou {} , empatou'.format(escolha,aleatorio))
elif escolha==1 and aleatorio==2:
    print('O jogador jogou PAPEL e o computador jogou TESOURA , jogador perdeu')
elif escolha==2 and aleatorio==1:
    print('O jogador jogou TESOURA e o computador jogou PAPEL , jogador GANHOU')
elif escolha==2 and aleatorio==0:
    print('O jogador jogou TESOURA e o computador jogou PEDRA , jogador PERDEU')
elif escolha == 0 and aleatorio == 2:
    print('O jogador jogou PEDRA e o computador jogou TESOURA , jogador GANHOU')
elif escolha>2:
    print('Jogada invalida.')