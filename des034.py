sal = float(input('Qual o valor do salario ? : '))
if sal > 1250:
    aumento = sal*(10/100)
    new_sal = sal+aumento
if sal <= 1250:
    aumento = sal * (15 / 100)
    new_sal = sal + aumento
print('Voce teve um aumento de \033[31m R$ {} \33[m , e seu novo salario é de \033[32m R$ {} \033[m'.format(aumento,new_sal))
