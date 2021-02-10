print(60*'=')
print('     LOJA BARATÃO     ')
print(60*'=')
total=0
cont_preco=0
menor_preco=0
menor_produto=' '
contador_produtos=0
while True:
    produto = input('Produto..........: ')
    preco = int(input('Preço........: '))
    total+=preco
    contador_produtos+=1
    if contador_produtos==1:
       menor_preco=preco
       menor_produto=produto
    else:
       if preco<menor_preco:
           menor_preco = preco
           menor_produto = produto
    if preco > 1000:
       cont_preco += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input(' Quer continuar  [S/N] : ')).upper().strip()[0]
    if resposta == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f' O total da compra foi R$ {total}')
print(f' Temos {cont_preco} custando mais de R$ 1000')
print(f' O produto mais barato foi {produto} custando R$ {menor_preco}. ')


