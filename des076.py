listagem = ('lapis', 1.75,
            'borracha' ,0.50,
            'caderno',10.00,
            'caneta',2.00,
            'lapizeira', 5.00,
            'papel a4', 9.00)
print('='*60)
print('>'*10, 'LISTAGEM DE PREÇOS','<'*10 )
print('='*60)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<50}', end=' ')
    else:
        print(f'R$ {listagem[pos]:>5.2f}')
print('='*60)