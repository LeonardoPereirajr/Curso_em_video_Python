cont=soma=media=maior=menor=0
op ='S'
while op =='S':
    n = int(input('Digite um numero : '))
    soma+=n
    cont+=1
    if cont==1:
        maior=menor=n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    op = str(input('Deseja continua ? [S/N] : ')).upper().strip()[0]
media=soma/cont
print(f'Voce digitou {cont} numeros , e sua media deu {media} ')
print(f' O maior valor foi {maior} e menor foi {menor} ')



