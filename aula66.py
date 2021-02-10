n=cont=s=0
while True:
    n = int(input('Digite um numero ou 999 para parar: '))
    if n==999:
        break
    s+=n
    cont+=1
print(f'Você digitou {cont} numeros e a soma entre eles dará {s} ')
