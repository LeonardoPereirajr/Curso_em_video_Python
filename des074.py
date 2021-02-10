import random
print('='*60)
print('>'*10, 'GERAR NUMERO ALEATORIOS','<'*10 )
ale= (random.randint(1,10),random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10))
print(ale)
if ale[0]>ale[1] and ale[0]>ale[2] and ale[0]>ale[3] and ale[0]>ale[4] :
    maior=ale[0]
elif ale[1]>ale[2] and ale[1]>ale[3] and ale[1]>ale[4]:
    maior = ale[1]
elif ale[2]>ale[3] and ale[2]>ale[4]:
    maior = ale[2]
elif ale[3]>ale[4]:
    maior=ale[3]
else:
    maior = ale[4]
if ale[0]<ale[1] and ale[0]<ale[2] and ale[0]<ale[3] and ale[0]<ale[4] :
    menor=ale[0]
elif ale[1]<ale[2] and ale[1]<ale[3] and ale[1]<ale[4]:
    menor = ale[1]
elif ale[2]<ale[3] and ale[2]<ale[4]:
    menor = ale[2]
elif ale[3]<ale[4]:
    menor=ale[3]
else:
    menor = ale[4]
print( f'O maior numero da sequencia é {maior}')
print( f'O menor numero da sequencia é {menor}')




