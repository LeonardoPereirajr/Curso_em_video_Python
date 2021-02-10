galera = list()
dado = list()
totmai=totmen=0
for c in range(0,3): ## pede 3 elementos
    dado.append(str(input('Nome : '))) ##adiciona dentro de dado
    dado.append(int(input('Idade: ')))## adiciona dentro de dado
    galera.append(dado[:]) ##coloca o conteudo de dado dentro da galera
    dado.clear() ##limpa dado
for p in galera:
    if p[1] >= 21:
        print(f' {p[0]} é maior de idade')
        totmai+=1
    else:
        print(f' {p[0]} é menor de idade')
        totmen+=1
print(f'Temos {totmai} maiores de idade e {totmen} menores de idade.')
