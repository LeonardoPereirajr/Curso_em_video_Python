soma = 0
for c in range(1,500):
    if c%2==1 and c%3==0:
        soma = soma+c
        print(c)
print(' A soma dos impares multiplos de 3 dara {}'.format(soma))
print('FIM ')