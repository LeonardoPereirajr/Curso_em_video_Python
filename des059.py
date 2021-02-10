n1 = int(input('Digite o 1º Valor : '))
n2 = int(input('Digite o 2º Valor : '))
soma = 0
multi=0
maior=0
opcao=0
print(10*'='+'MENU'+10*'=')
print(' [  1  ]  SOMAR ')
print(' [  2  ]  MULTIPLICAR ')
print(' [  3  ]  MAIOR ')
print(' [  4  ]  NOVOS NUMEROS ')
print(' [  5  ]  SAIR DO PROGRAMA ')
while opcao !=5 :
    opcao = int(input('Qual opção vocÊ deseja executar ? '))
    if opcao==1:
        print(' VAMOS SOMAR!!!')
        print('A soma de {} + {} dara {}'.format(n1,n2,n1+n2))
    elif opcao==2:
        print(' VAMOS MULTIPLICAR!!!')
        print('A multiplicação de {} X {} dara {}'.format(n1, n2, n1 * n2))
    elif opcao==3:
        print(' VAMOS VER QUAL MAIOR NUMERO!!!')
        if n1>n2:
            maior=n1
        else:
            maior=2
            print('O maior numero entre  {} e {} é {}'.format(n1, n2, maior))
    elif opcao==4:
        print('OK Vamos digitar novos numeros!!!')
        n1 = int(input('Digite o 1º Valor : '))
        n2 = int(input('Digite o 2º Valor : '))
print(' VOCÊ DIGITOU PARA SAIR!!!')




