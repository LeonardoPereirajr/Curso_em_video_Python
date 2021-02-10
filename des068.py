import random
from time import sleep
aleatorio = random.choice(range(0,9999))
print(aleatorio)
print(20*'=')
print(" JOGO DE PAR OU IMPAR")
print(20*'=')
cont=0
escolha = int(input("Digite um numero : "))
opcao = str(input('O Resultado será par ou impar ? :')).upper()
print('PROCESSANDO...')
sleep(2)
soma = (aleatorio+escolha)
if soma%2==0:
    resultado='PAR'
else:
    if soma%2==1:
        resultado='IMPAR'
print(soma)
print(resultado)
while resultado==opcao:
    print(f'Voce acertou o numero era {aleatorio}, voce digitou {escolha}, a soma deu {soma} que é um numero {resultado}')
    cont+=1
    escolha = int(input("Tente novamente outro numero : "))
    opcao = str(input('O Resultado será par ou impar ? :')).upper()
print(f'Voce errou numero era {aleatorio}, voce digitou {escolha}, a soma deu {soma} que é um numero {resultado}')
print(f'Game over. Voce ganhou {cont} partida')
print(20*'=')