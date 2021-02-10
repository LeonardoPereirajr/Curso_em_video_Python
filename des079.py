lista=[]
while True:
    n = int(input('Digite um valor : ')) ## precisa colocar o valor em uma variavel para procurar na lista
    if n not in lista: ## ver se n esta na lista
       lista.append(n) # acrescenta n na lista
       print('Valor adicionado com sucesso')
    else:
       print('Numero ja existe.')
    res = str(input('Deseja continuar ? [S/N] : '))
    if res in 'Nn':
        break
lista.sort() # organiza em ordem crescente
print(f'Voce digitou os os valores {lista}')
