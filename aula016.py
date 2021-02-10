lanche = 'hamburguer','suco','pizza','pudim','batata frita'
print(lanche [1])##suco
print(lanche [2])##pizza
print(lanche [3])##pudim
print(lanche [0])##hamburguer
print(lanche [-2])##pizza
print(lanche[1:3])##suco e pizza
print(lanche [2:])##pizza e pudim
print(lanche [:2])##hamburguer e suco
print(lanche [-2:])##pizza e pudim
print(lanche [-3:])##suco pizza e pudim
print(len(lanche))## 4
print('=' *60)

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi para caramba')
print('=' *60)

for cont in range(0, len(lanche)):
    print(f' Eu vou comer {lanche[cont]}')
print('Comi para caramba')
print('=' * 60)

## colocando a posição

for pos , comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi para caramba')
print('=' *60)

for cont in range(0, len(lanche)):
    print(f' Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi para caramba')
print('=' * 60)

#mostra ordenado
print(sorted(lanche))
print('=' * 60)

a= 2,5,4
b=5,8,1,2
c=b+a
print(c)# apresenta a colagem de tuplas
print('=' * 60)
print(len(c))## quantos elementos ha
print('=' * 60)
print(c.count(5))
print('=' * 60)
print(c.index(8))## em qual posição esta o 8
print('=' * 60)
print(c.index(2))## em qual posição esta a 1ª ocorrencia de 2
print('=' * 60)
print(c.index(5))## em qual posição esta a 1ª ocorrencia de 5
print('=' * 60)
print(c.index(5,1))## em qual posição esta a proxima ocorrencia de 5
print('=' * 60)
pessoa='gustavo',39,'masculino', 99.88
print(pessoa)



