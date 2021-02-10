lista = []
lista_par = []
lista_impar = []
while True:
    lista.append(int(input('Digite os numeros: ')))
    res = str(input('Quer continuar [S/N] : '))
    if res in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        lista_par.append(v)
    else:
        lista_impar.append(v)
print(f'O numeros da lista fora : {lista}')
print(f'O numeros pares foram  : {lista_par}')
print(f'O numeros impares foram : {lista_impar}')