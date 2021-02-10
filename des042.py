l1 = float(input('Digite o primeiro lado :'))
l2 = float(input('Digite o segundo lado :'))
l3 = float(input('Digite o terceiro lado :'))
if (l1+l2) > l3 and (l2+l3)>l1 and (l1+l3)>l2:
    print('Forma um triangulo')
    if l1==l2 and l2==l3:
        print("Forma um triangulo Equilatero")
    elif l1!=l2!=l3!=l1  :
        print("Forma um triangulo escaleno")
    else:
        print("Forma um triangulo Isosceles")
else:
    print('NÃO Forma um triangulo')