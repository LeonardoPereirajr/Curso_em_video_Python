import random
palavras = 'hamburguer','suco','pizza','pudim'
print('='*60)
escolha = str(random.choice(palavras))
espacos= len((escolha))
print(espacos*'-')
print(escolha)
erro=0
acerto=0
letra=''
while erro<5:
    letra=(str(input('Qual letra você escolhe ? : ')))
    if letra in escolha:
        print(f'Na palavra há a letra {letra} na posição {escolha.index(letra)+1}')
        if acerto==len(escolha):
            print(f'Você acertou a palavra era {escolha}')
    else:
        erro+=1
        if erro<5:
            print('Tente novamente')
        else:
            if erro>=5:
                print('Voce perdeu com as 5 chances')
    acerto = +1
    print(acerto)
'''
for pos in escolha:
    print(f'\nNa palavra {pos.upper()} temos', end =" ")
    for letra in pos:
        if letra.lower() in 'aeiou':
            print(letra, end = ' ')'''