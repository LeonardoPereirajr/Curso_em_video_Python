numeros=[[0,0,0], [0,0,0], [0,0,0]]
soma=0
coluna=linha=maior=0
for l in range(0,3):
   for c in range(0,3):
      numeros[l][c] = int(input(f' Digite um valor para [ {l},{c} ] : '))
print('+='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{numeros[l][c]:^6}]', end='')
        if numeros[l][c] % 2 ==0:
            soma+=numeros[l][c]
    print()
for c in range(0,3):
    coluna+=numeros[c][2]
    c+=1
for l in range(0,3):
    linha+=numeros[1][l]
    l+=1
for l in range(0,3):
    if numeros[1][l] > maior:
        maior=numeros[1][l]
        l+=1
print(f'A Soma dos numeros pares é {soma}')
print(f'A soma da 3ª coluna é {coluna}')
print(f'A soma da 2ª linha é {linha}')
print(f'A maior numero da 2ª linha é {maior}')


