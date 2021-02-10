import math
num = int(input('DIGITE O NUMERO para calcular o fatorial : '))
c = num
print('Calculando {}! = '.format(num), end='')
while c > 0 :
    print(' {} '.format(c), end=' ')
    print('x' if c > 1 else '=', end = ' ')
    c-=1
print(math.factorial(num))