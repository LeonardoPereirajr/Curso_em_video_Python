import random
print('='*60)
print('>'*10, 'GERAR NUMERO ALEATORIOS','<'*10 )
ale= (random.randint(1,10),random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10))
print(ale)
print( f'O maior numero da sequencia é {max(ale)}')
print( f'O menor numero da sequencia é {min(ale)}')