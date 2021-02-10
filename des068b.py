from random import randint
aleatorio = randint(0,10)
print(aleatorio)
print(20*'=')
print(" JOGO DE PAR OU IMPAR")
print(20*'=')
cont=0
escolha = int(input("Digite um numero : "))
soma = (aleatorio+escolha)
opcao = ' '
while opcao not in 'PI':
    opcao = str(input('O Resultado será par ou impar ? :')).strip().upper()[0]
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