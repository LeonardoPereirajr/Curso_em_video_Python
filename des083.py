lista=[]
ex = (str(input('Digite uma expressão numerica :  ')))
for c in ex:
    lista.append(c)
n1 = lista.count('(')
n2 = lista.count(')')
if n1==n2:
    print('A expressão é valida.')
else:
    print('A expressão é invalida.')
