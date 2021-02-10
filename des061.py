print('=====PROGRESSÃO ARITMETICA====')
p = int(input('Qual o primeiro termo : '))
razao = int(input('Qual a razão : '))
c=1
print(p,'->', end= '')
while c <= 10:
    p = p+razao
    c+=1
    print(' {} ->'.format(p), end =' ')
print('FIM')