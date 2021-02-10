'''from datetime import date
ano = date.today().year'''
soma_idade=0
idade_masc=0
cont_mul=0
cont_idade=0
for c in range(1,5):
    print('+=+=+=+= {}a PESSOA +=+=+=+='.format(c))
    nome=input('NOME.:::: ')
    idade=int(input('IDADE.:::: '))
    sexo=input('SEXO [M/F} : ')
    soma_idade+=idade
    media=soma_idade/4
    if sexo=='M' and idade>idade_masc:
            idade_masc=idade
            velho=nome
    elif sexo == 'F' and idade<20:
        cont_mul= cont_mul+1
        cont_idade=cont_idade+1
print('A media de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {} .'.format(idade_masc,velho))
print(' Ao todo são {} mulheres com menos de 20 anos.'.format(cont_mul))



