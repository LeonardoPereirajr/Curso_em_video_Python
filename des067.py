print(15*'=')
print('>>>>>>>TABUADA<<<<<<<')
print(15*'=')
n = int(input('Quer ver a tabuada de qual valor? : '))
resp=' '
while n>0:
    for c in range(0,10):
        c = c + 1
        res = n * c
        print(n, ' x ', c, ' = ', res)
    resp = str(input('Deseja continuar :[S/N] : '))
    if resp == 'N':
        break
    else:
        n = int(input('Digite um numero : '))
print(15*'=')
