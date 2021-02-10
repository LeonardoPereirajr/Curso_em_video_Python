cont_p= 0
c = str(input("Digite o sexo da pessoa [F/M] : ")).strip().upper()[0]
while c not in 'MF':
    c = str(input("Dados invalidos .Digite o sexo da pessoa [F/M] : ")).strip().upper()[0]
print('Sexo {} registrado com sucesso '.format(c))