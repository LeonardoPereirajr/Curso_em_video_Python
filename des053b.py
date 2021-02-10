texto = str(input('Digite um texto : ')).strip().upper()
'''gerando a lista'''
palavras = texto.split()
'''juntar a lista para eliminar espaços'''
junto = ''.join(palavras)
inv = ''
'''trocar as letras'''
for letra in range(len(junto)-1,-1,-1):
    inv +=junto[letra]
print(junto,inv)
if junto==inv:
    print('O inverso de "{}" é "{}" e ele é um palindromo'.format(texto, inv))
else:
    print(' O inverso de "{}" é "{}"  e ele não é um palindromo'.format(texto, inv))