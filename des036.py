casa = int(input('Qual o valor da casa? '))
sal = int(input('Qual seu salario? '))
prazo = int(input('Quantos meses deseja pagar ? '))
parcela = casa/prazo
margem = sal* (30/100)
if parcela > margem:
    print('Este negocio não foi aprovado, aumente o prazo .')
else:
    print("Negocio aprovado pois a parcela é de R$ {} e voce pode pagar R$ {} mensais".format(parcela,margem))
