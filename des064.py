cont = soma = vezes=0
op =int(input('Deseja continua ? [999] para encerrar senão digite outro numero : '))
while op !=999:
    soma+=op
    vezes+=1
    op = int(input('Deseja continua ? [999] para encerrar senão digite outro numero : '))
print('A soma dos {} numeros digitados foi {}'.format(vezes,soma))