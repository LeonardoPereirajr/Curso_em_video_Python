print('='*60)
print('>'*10, 'ANALISADOR DE NUMEROS','<'*10 )
print('='*60)
n = (int(input('Digite um numero de 0 a 10 : ')),
     int(input('Digite outro numero de 0 a 10 : ')),
     int(input('Digite mais um numero de 0 a 10 : ')),
     int(input('Digite o ultimo numero de 0 a 10 : ')))
print(f'voce digitou os valores {n}')
if 9 in n:
    print(f'O valor 9 apareceu {n.count(9)} vezes')
else:
    print('O valor 9 não foi digitado')
if 3 in n:
    print(f' O numero 3 apareceu a 1º vez na posição {n.index(3)+1}')
else:
    print('O valor 3 não foi digitado')
print(' Os valores pares digitados foram somente ', end=' ')
for c in n:
    if c%2==0:
        print(c,'-', end=' ')




