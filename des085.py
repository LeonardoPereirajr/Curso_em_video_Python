numeros=[]
valor=0
pares=[]
impares=[]
principal=[]
for c in range(1,8):
    numeros.append(int(input(f' Digite o {c}º valor: ')))
print(numeros)
for p in numeros:
    if p % 2 == 0:
        pares.append(p)
        pares.sort()
    if p % 2 == 1:
        impares.append(p)
        impares.sort()
principal.append(pares[:])
principal.append(impares[:])
print(principal)


