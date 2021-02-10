texto = input('Digite um texto : ').upper()
espaco = texto.replace(' ', '')
inv = espaco[::-1]
if espaco==inv:
    print('O inverso de "{}" é "{}" e ele é um palindromo'.format(texto, inv))
else:
    print(' O inverso de "{}" é "{}"  e ele não é um palindromo'.format(texto, inv))