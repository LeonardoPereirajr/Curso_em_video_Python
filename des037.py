num = int(input('Qual o numero que deseja converter ? '))
print(' [  1  ]  BINARIO ')
print(' [  2  ]  OCTAL ')
print(' [  3  ]  HEXADECIMAL ')
res = int(input('Em que formato deseja converter ? 1/2/3 : '))
if res == 1:
    print(' O numero {} em Binario é {} .'.format(num,bin(num)))
elif res==2:
    print(' O numero {} em Octal é {} .'.format(num,oct(num)))
elif res==3:
    print(' O numero {} em Hexadecimal é {} .'.format(num, hex(num)))