pessoas=[]
cadastro={}
sexo_fem = []
sexo_mas = []
mulheres=[]
homens=[]
idades=[]
media=0
while True:
    nomes = str(input('Nome : '))
    pessoas.append(nomes)
    sexo = str(input('Sexo: '))
    if 'F' in sexo:
        mulheres.append(nomes)
        sexo_fem.append(sexo)
    else:
        if 'M' in sexo:
            homens.append(nomes)
            sexo_mas.append(sexo)
    idade = int(input('Idade : '))
    idades.append(idade)
    cadastro['nomes']= pessoas
    cadastro['homens'] = homens
    cadastro['mulheres'] = mulheres
    cadastro['idades'] = idades
    media = sum(idades) / len(cadastro["nomes"])
    if idade >= media:
        nome_acima = nomes
    res = str(input('Quer continuar [S/N] : '))
    if res in 'Nn':
        break
print(cadastro)
print(f'A) O grupo tem {len(cadastro["nomes"])} pessoas. ')
print(f'B) A media de idades é { sum(idades)/len(cadastro["nomes"])}')
print(f'C) As mulheres cadastradas foram:  {cadastro["mulheres"]}.')
print('D) Lista das pessoas que estão acima da media: ', end = '')
print(nome_acima, ' ')
