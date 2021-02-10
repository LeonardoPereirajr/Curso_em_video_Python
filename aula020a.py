def soma(a,b):
    print(f' A = {a} e B = {b}')
    s = a+b
    print(f' A soma A + B = {s}')


# PRINCIPAL
soma(4, 5)

print(30*'++')
# EXEMPLO COM EMPACOTAMENTO
def contador(* num):
    tam = len(num)
    print(f' Recebi os valores {num} e são ao todo {tam} numeros. ')


contador(2,1,7)
contador(8,0)
contador(4,4,7,6)
print(30*'++')

# EXEMPLO COM DESEMPACOTAMENTO
def somando(* valores):
    s = 0
    for num in valores:
        s += num
    print(f' Somando os valores {valores} temos {s}')

somando(5,2)
somando(2,9,4)

print(30*'++')

# EXEMPLO COM LISTA
def dobra(lst):
    pos=0
    while pos<len(lst):
        lst[pos]*=2
        pos +=1

valores = [6,3,9,1,0,2]
dobra(valores)
print(valores)


