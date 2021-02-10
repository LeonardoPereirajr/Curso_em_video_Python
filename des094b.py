pessoa ={}
galera = []
soma = media = 0
## CAPTURA DE DADOS
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F] :')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! por favor digite M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar ? [S/N]')).upper()[0]
        if resp in "SN":
            break
        print('ERRO! por favor digite S ou N')
    if resp == 'N':
        break
##FIM DA CAPTURA DE DADOS
print('=+'*30)
print(galera)
##VISUALIAZAR DADOS
print(f' A) Ao todo temos {len(galera)}, pessoas cadastradas')
media = soma / len(galera)
print(f' B) A media de idade é de {media:5.2f} anos')
print(' C) As mulheres cadastradas foram', end = '')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f' {p["nome"]}', end =' ')
print()
print(' D) Lista das pessoas que estão acima da media: ')
for p in galera:
    if p['idade']>=media:
        print('    ')
        for k, v in p.items():
            print(f' {k} = {v}', end = '')
        print()
print('<<ENCERRADO>>')