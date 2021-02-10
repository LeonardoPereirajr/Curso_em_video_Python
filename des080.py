val = []
for c in range(0,5):
    n = int(input('Digite um valor : '))## espera digitar elementos
    if c == 0 or n > val[-1]:
        val.append(n)
        print('Adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(val):## ENQUANTO POS MENOR QUE O TAMANHO DA LISTA
            if n <= val[pos]:##VER SE O NUMERO É MENOR QUE O VALOR NA POSIÇÃO VERIFICADA
                val.insert(pos,n)##COLOCA NA POSIÇÃO "POS" O VALOR N
                print(f'Adicionado {n} na posição {pos}')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados foram {val}')
