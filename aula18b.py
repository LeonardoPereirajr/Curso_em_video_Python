galera = [['Joao', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[3][1])
for p in galera:## para cada posição em galera mostre na tela
    print(p)
print('-+'*30)
for p in galera:##mostra os nomes
    print(p[0])
print('-+' * 30)
for p in galera:##mostra os numeros
    print(p[1])
print('-+' * 30)
for p in galera:##mostra os dois
    print(f'{p[0]} tem {p[1]} anos de idade.')
print('-+' * 30)