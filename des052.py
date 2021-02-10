num = int(input('Digite um numero : '))
tot=0
for c in range(1,num + 1):
    if num % c == 0 :
        print(' {} '.format(c))
        tot +=1
    else:
        print('{} '.format(c))