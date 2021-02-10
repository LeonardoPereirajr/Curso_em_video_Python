valores=[]
maior=menor=pos_cont1=0
pos_cont2=0
print(30*'=+')
for cont in range(0,5):
    valores.append(int(input(f'Digite um valor na posição {cont}: ')))
    if cont==0:
       maior=menor=valores[0]
    else:
       if valores[cont]>maior:
          maior=valores[cont]
       if valores[cont]<menor:
           menor=valores[cont]
print(f'Voce digitou os valores {valores}')
print(f' O maior valor encontrado foi {maior} nas posição ', end = '')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end= '')
print()
print(f' O menor valor encontrado foi {menor} encontrado na posição ', end = '')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end= '')
print()

