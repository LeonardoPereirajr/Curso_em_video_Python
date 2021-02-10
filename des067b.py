print(20*'=')
print('>>>>>>>TABUADA<<<<<<<')
print(20*'=')
resp=' '
while True:
    n = int(input('Quer ver a tabuada de qual valor? : '))
    if n < 0:
        break
    print(30 * '=')
    for c in range(0,10):
        c = c + 1
        print(f' {n} x {c} = {n*c}')
    print(30 * '=')
print(50*'=')
print('Voce digitou um numero negativo e neste caso o programa encerrou.')
print(50*'=')