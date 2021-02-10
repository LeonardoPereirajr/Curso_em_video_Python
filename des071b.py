n = int(input('Qual valor você quer sacar: R$'))
if n // 50 != 0:
    a = n // 50
    n %= 50
    print(f'Total de {a} cédulas de R$50')
if n != 0 and n // 20 != 0:
    b = n // 20
    n %= 20
    print(f'Total de {b} cédulas de R$20')
if n != 0 and n // 10 != 0:
    c = n // 10
    n %= 10
    print(f'Total de {c} cédulas de R$10')
if n != 0:
    print(f'Total de {n} cédulas de R$1')