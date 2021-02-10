ficha =[]
while True:
    nome = str(input('Nome : '))
    nota1 = float(input('Nota 1 : '))
    nota2 = float(input('Nota 2 : '))
    media = (nota1+nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    res = str(input('Quer continuar [S/N] : '))
    if res in 'Nn':
        break
print(ficha)