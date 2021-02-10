tupla='zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez'
while True:
    n = int(input('Digite um numero de 0 a 10 : '))
    if 0 <= n <=10:
        break
    print('Digite um numero de 0 a 10 :', end='')
print(f'Voce digitou {tupla[n]} no teclado')

