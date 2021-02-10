##listas
num = [2,5,9,1]
num[2]=3## colocar 3 na posição 2
num.append(7)##acrescentar 7
##num.sort() ##ordena
num.insert(2,0)
print(num)
##num.sort(reverse=True)## ordena ao contrario
print(f'Essa lista possui {len(num)} elementos')## mostra quantos elementos há
num.pop(2) ##apaga um elemento
print(num)
num2 =[7,5,2,3,4]
num2.insert(2,2)## insere um elemento em determinada posição
num2.remove(2)## remove determinado elemento se ele existir
if 4 in num2:
    num2.remove(4)
else:
    print('Não achei o numero 4')
print(num2)
print(60*'=+')
valores=[] ##cria lista vazia e insere elementos
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)
print(60*'=+')
for v in valores:
    print(f'{v}...' )## coloca elementos embaixo
print(60*'=+')
for c, v in enumerate(valores):
    print(f'na posição {c} encontrei o valor {v} !')#mostra elementos encontrados
print('Cheguei no final da lista')
print(60*'=+')
valores2=list()
for cont in range(0,5):
    valores2.append(int(input('Digite um valor : ')))## espera digitar elementos
for c, v in enumerate(valores2):
    print(f'na posição {c} encontrei o valor {v} !')
print('Cheguei no final da lista')
print(60*'=+')
a=[2,3,4,7]
b=a[:]## cria uma copia
b[2]=8
print(f' lista A : {a}')
print(f' lista B : {b}')




