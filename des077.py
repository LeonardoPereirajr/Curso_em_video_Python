lanche = 'hamburguer','suco','pizza','pudim'
for pos in lanche:
    print(f'\nNa palavra {pos.upper()} temos', end =" ")
    for letra in pos:
        if letra.lower() in 'aeiou':
            print(letra, end = ' ')