nome = input('digite seu nome : ').strip()
print('Maiusculas : {} '.format(nome.upper()))
print('Minusculas:  {} '.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('seu primeiro nome é {} '.format(nome[0:nome.find(' ')]))
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0],len(separa[0])))






