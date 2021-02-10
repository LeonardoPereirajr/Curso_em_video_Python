aluno={}
aluno['Nome']=str(input(' Nome : '))
aluno['Média'] = float(input(f' Média de {aluno["Nome"]} : '))
print('=-'*30)
if aluno["Média"] > 7:
    aluno['situacao'] = 'aprovado'
else:
    if aluno["Média"] <= 5:
        aluno['situacao'] = 'reprovado'
    else:
        aluno['situacao'] = 'recuperacao'
for k, v in aluno.items():
    print(f' - {k} é igual a {v} .')
