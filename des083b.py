pilha=[]
ex = (str(input('Digite uma expressão numerica :  ')))
for simb in ex:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha)> 0 :
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0 :
    print('A expressão é valida.')
else:
    print('A expressão é invalida.')