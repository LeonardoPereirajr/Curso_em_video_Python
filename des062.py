print('=====PROGRESSÃO ARITMETICA====')
p = int(input('Qual o primeiro termo : '))
razao = int(input('Qual a razão : '))
termo = p
c = 1
mais=10
total=0
while mais !=0:
    total+=mais
    while c <= total:
        print(' {} ->'.format(termo), end =' ')
        termo+=razao
        c+=1
    print('pausa')
    mais = int(input("Quantos termos você quer mostrar a mais ? "))
print('A progressão foi finalizada com {} termo mostrados '.format(total))


