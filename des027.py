n = str(input('Digite seu nome : ').strip())
nome = n.split()
print(' Seu primeiro nome é {} '.format(n[0:n.find(' ')]))
print(' Seu ultimo nome é {} '.format(nome[len(nome)-1]))

