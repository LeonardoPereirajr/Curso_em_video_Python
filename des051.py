print('=====PROGRESSÃO ARITMETICA====')
primeiro = int(input('Qual o primeiro termo : '))
razao = int(input('Qual a razão : '))
decimo = primeiro + (10-1)*razao
print(10*'=')
for c in range(primeiro,decimo + razao,razao):
    print(' {} '.format(c), end ='->')