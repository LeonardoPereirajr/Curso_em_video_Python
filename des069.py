print(60*'=')
print('     CADASTRE UMA PESSOA     ')
print(60*'=')
idade=0
sexo=''
cont_idade=0
cont_sexo=0
cont_mulher=0
idade=int(input('Idade... : '))
sexo=str(input('Sexo [M/F] : ')).upper()
if idade > 18:
    cont_idade += 1
if sexo == 'M':
    cont_sexo += 1
elif sexo == 'F':
    if idade > 20:
        cont_mulher += 1
resposta = str(input(' Quer continuar  [S/N] : ')).upper()
while resposta=='S':
    print(60 * '=')
    idade = int(input('Idade... : '))
    sexo = str(input('Sexo [M/F] : ')).upper()
    if idade>18:
        cont_idade+=1
    if sexo =='M':
        cont_sexo+=1
    elif sexo=='F':
        if idade<20:
           cont_mulher+=1
    resposta = str(input(' Quer continuar  [S/N] : ')).upper()
print(f' O total de pessoas com mais de 18 anos é {cont_idade}')
print(f' Ao todo temos {cont_sexo} homens cadastrados')
print(f' Temos {cont_mulher} mulher com menos de 20 anos. ')