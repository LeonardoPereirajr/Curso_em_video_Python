from datetime import date
funci={}
funci['Nome']=str(input(' Nome : '))
ano_nasc = int(input(f' Ano de Nasc. : '))
idade = date.today().year - ano_nasc
funci['idade'] = idade
funci['CTPS'] = int(input(f' Numero da CTPS.(0 não tem) :  '))
if funci['CTPS'] > 0:
    funci['contrato'] = int(input(f' Ano de Contratação. : '))
    aposentar_idade = (idade + (35 - (date.today().year - funci['contrato'])))
    funci['aposentadoria']=aposentar_idade
    funci['salario'] = float(input(f' Salario  : '))
print('=+'*30)
print(funci)
print('=+'*30)
for k, v in funci.items():
        print(f' {k} tem valor {v} ')
