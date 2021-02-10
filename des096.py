def area(a,b):
    medida = a*b
    print(f'A area de um terreno {a} x {b} é de {medida} m² ')


def mostralinha():
    print(30*'-+-')


# PRINCIPAL
mostralinha()
print(' CONTROLE DE TERRENOS')
mostralinha()
l = float(input('LARGURA (m) : ' ))
c = float(input('COMPRIMENTO (m) : '))
area(l,c)


