import random
from time import sleep
print('=+'*30)
print('                JOGO DA MEGA SENA         ')
print('=+'*30)
quant=(int(input('Quantos jogos você quer sortear?  :  ')))
lista=[]
jogos=[]
cont=tot=0
l=0
while tot<= quant-1:
    cont = 0
    while True:
        numeros = random.randint(1, 60)
        if numeros not in lista:
            lista.append(numeros)
            cont+=1
            if cont>=6:
                break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot+=1
for n in range(0,quant):
    print(f' JOGO {n+1}: {jogos[n]}')
    sleep(2)
