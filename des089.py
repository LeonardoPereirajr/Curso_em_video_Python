consulta=[]
tot=0
classe=[]
sala=[]
media=[]
while True:
    aluno = str(input('Nome : '))
    nota1 =float(input('Nota 1: '))
    nota2 = float(input('Nota 2 : '))
    media = (nota1+nota2)/2
    classe.append([aluno, [nota1, nota2], media])
    tot+=1
    res = str(input('Quer continuar [S/N] : '))
    if res in 'Nn':
        break
print(classe[0][1])
print('=+'*40)
print(f'{"No.":<4} {"NOME":>10} {"NOTAS":>8}')
print('--'*40)
for i, a in enumerate(classe):
    print(f' {i:<4} {a[0]:<10} {a[2]:>8.1f} ')
print('=+'*40)
while True:
    boletim = int(input('Deseja ver as notas de qual aluno : [999 interrompe] '))
    if boletim == 999:
        print('FINALIZANDO...')
        break
    if boletim <= len(classe)-1:
        print(f' Notas de {classe[boletim][0]} são {classe[boletim][1]}')
print('FIM')