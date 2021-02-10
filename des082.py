lista = []
lista_par = []
lista_impar = []
while True:
    n = (int(input('Digite os numeros: ')))
    lista.append(n)
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)
    res = str(input('Quer continuar [S/N] : '))
    if res in 'Nn':
       break
print(f'O numeros da lista fora : {lista}')
print(f'O numeros pares foram  : {lista_par}')
print(f'O numeros impares foram : {lista_impar}')