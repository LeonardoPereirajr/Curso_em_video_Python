frase = str(input('digite uma frase : ').strip().upper())
print(' A letra A aparece {} vezes na frase a primeira vez é na {} posição e a ultima é na posição {}'.format(frase.count('A'), frase.find('A')+1,frase.rfind('A')+1))
