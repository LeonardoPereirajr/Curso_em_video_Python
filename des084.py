temp=list()
princ=[]
mai = 0
men = 0
while True:
    temp.append(str(input('Nome : ')))  ##adiciona
    temp.append(float(input('Peso: ')))  ## adiciona
    if len(princ) == 0: ## se é a primeira pessoa entao o maior e o menor peso serão iguais
        mai = men = temp[1] ## aqui olha-se a referencia [nome,peso] = [0,1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()##precisa limpar porque senao duplica
    res = str(input('Quer continuar [S/N] : '))
    if res in 'Nn':
       break
print('=+'*30)
print(f'Foram encontradas {len(princ)} pessoas.')
print(f'O maior peso encontrado foi {mai} kg. peso de ' , end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso encontrado foi {men}. ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()