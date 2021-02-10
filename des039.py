from datetime import date
ano = int(input('ANO de nascimento :  '))
ano_hoje = date.today().year
cont = ano_hoje - ano
if cont > 20 :
    print(' Quem nasceu em {} tem {} anos  em {} . '.format(ano, cont, ano_hoje))
    print(' Sua classificação é MASTER. ')
elif cont == 20  :
    print(' Quem nasceu em {} tem {} anos  em {} . '.format(ano, cont, ano_hoje))
    print(' Sua classificação é SENIOR. ')
elif cont >= 19 :
    print(' Quem nasceu em {} tem {} anos  em {} . '.format(ano, cont, ano_hoje))
    print(' Sua classificação é JUNIOR. ')
elif cont >=10 :
    print(' Quem nasceu em {} tem {} anos  em {} . '.format(ano, cont, ano_hoje))
    print(' Sua classificação é INFANTIL. ')
elif cont <= 9 :
    print(' Quem nasceu em {} tem {} anos  em {} . '.format(ano, cont, ano_hoje))
    print(' Sua classificação é MIRIM. ')