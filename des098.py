import time
def contador(i,f,p):
    print(30*'+')
    print(f'Contagem de {i} ate {f} de {p} em {p}')
    if p < 0:
        p*=-1
    if p == 0:
        p = 1
    if i<f:
        cont = i
        while cont <=f:
            print(f'{cont} ', end = '')
            cont+=p
            time.sleep(0.5)
        print('FIM!')
    else:
        cont = i
        while cont>= f:
            print(f'{cont} ', end='')
            cont -= p
            time.sleep(0.5)
        print('FIM!')


#PRINCIPAL
contador(1,10,1)
contador(10,0,2)
print(30 * '+')
print('Agora é sua vez de personalizar a contagem.')
ini = int(input('INICIO : '))
fim = int(input('FIM : '))
pas = int(input('PASSO : '))
contador(ini,fim,pas)

