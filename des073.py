tupla = 'Palmeiras','Cruzeiro','Grêmio','Santos','Corinthians','Flamengo','Atlético Mineiro','Athletico Paranaense','Internacional','Chapecoense','Botafogo','São Paulo','Fluminense',\
        'Vasco da Gama','Bahia','Sport','Vitória','Ponte Preta','América','Coritiba'
print('='*60)
print('>'*10, 'CINCO PRIMEIROS','<'*10 )
print(tupla[0:5])
print('='*60)
print('>'*10, 'QUATRO ULITMOS','<'*10 )
print(tupla[-4:])
print('='*60)
print('>'*10, 'ORDEM ALFABETICA','<'*10 )
print(sorted(tupla))
print('='*60)
print('>'*10, 'POSIÇÃO DA CHAPECOENSE','<'*10 )
pos = tupla.index('Chapecoense')
print(f'A Chapecoense esta na {pos} ª posição do ranking')

