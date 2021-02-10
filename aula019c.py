estado={}
brasil=[]
for c in range(0,3):
    estado['uf']=str(input('Unidade Federativa : '))
    estado['sigla'] = str(input('Sigla do estado : '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    print(e)
for e in brasil:
    for k, v in e.items():
        print(f' O Campo {k} tem valor  {v}')
for e in brasil:
    for v in e.values():
        print(v, end ='')
    print()