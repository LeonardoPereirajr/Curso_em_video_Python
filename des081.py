lista=[]
while True:
    lista.append(int(input('Digite um valor : ')))
    res = str(input('Deseja continuar ? [S/N] : '))
    if res in 'Nn':
       break
print('+='*30)
print(f'Voce digitou {len(lista)} numeros')
lista.sort(reverse=True)  # organiza em ordem crescente
print(f'Voce digitou em ordem decrescente valores {lista}')
if 5 in lista:
    print('O valor 5 esta na lista')
else:
    print('O valor 5 nao esta na lista')