def funcao():
    global n1
    n1 = 4
    print(f' n1 dentro vale {n1}')


n1 = 2
funcao()
print(f' n1 global vale {n1}')