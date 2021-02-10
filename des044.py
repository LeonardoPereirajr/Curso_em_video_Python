print(5*'=='+ 'LOJAS GUANABARA'+ 5*'==')
compra = int(input('Qual valor da compra ? R$  '))
print('FORMAS DE PAGAMENTO')
print('[ 1 ]  A VISTA DINHEIRO')
print('[ 2 ]  A VISTA CARTAO')
print('[ 3 ]  2X CARTAO')
print('[ 4 ]  3X OU MAIS NO CARTAO')
pag = int(input('Qual a forma de pagamento ? : '))
if pag == 1  :
    print('Sua compra a vista de R$ {} recebeu 10% de desconto e será de {:.2f}'.format(compra,compra-(compra*(10/100))))
elif pag == 2  :
    print('Sua compra a vista no cartão , de R$ {} recebeu 5% de desconto e será de {:.2f}'.format(compra,compra-(compra*(5/100))))
elif pag== 3 :
    print('Sua compra de 2x no cartão , de R$ {} ficara {} mensal . '.format(compra,compra/2))
else:
    print('Sua compra no cartão , de R$ {} terá um acrescimno de 20% e será de {:.2f}'.format(compra,compra+(compra*(20/100))))