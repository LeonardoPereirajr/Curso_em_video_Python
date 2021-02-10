import random
numeros=[]

def sorteia():
    cont = 0
    while True:
        valores = random.randint(1, 100)
        if valores not in numeros:
           numeros.append(valores)
           cont += 1
           if cont >= 5:
              break
    print(f'Os numeros escolhidos foram {numeros} .' )

def somaPar():
    pares=[]
    soma=0
    for p in numeros:
        if p % 2 == 0:
            pares.append(p)
    print(f' Os numeros pares foram  {pares}')
    for p in pares:
        soma+=p
    print(f' A soma dos pares dará {soma}')


sorteia()
somaPar()
