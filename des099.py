def contador(* valor):
    print(f'Foram informados {len(valor)} valores ')
    s = 0
    num_maior = 0
    for num in valor:
        if num==0:
            num_maior=valor
        else:
            if num > num_maior:
                num_maior=num
    print(f' Dentre os valores {valor} temos {num_maior} como sendo o maior')


def mostralinha():
    print(30*'-+-')


# PRINCIPAL
contador(2,22,9,7,8)
mostralinha()
contador(3,7,8,9,123,4,5678)
mostralinha()
contador(245,87,9273,88991,182)
mostralinha()
contador()
mostralinha()
contador(0)