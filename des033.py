n1 = input('Digite o n1 : ')
n2 = input('Digite o n2 : ')
n3 = input('Digite o n3 : ')
if n1>n2 and n1>n3:
    maior=n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
if n1<n2 and n1<n3:
    menor=n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print(' O maior numero é  {} : '.format(maior))
print(' O menor numero é  {} : '.format(menor))


