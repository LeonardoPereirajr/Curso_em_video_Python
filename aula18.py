teste = list() ##cria a lista teste
teste.append('Gustavo')##adiciona na lista
teste.append(40)##adiciona na lista
galera = list()##cria outra lista
galera.append(teste[:])## coloca dentro de galera a lista teste como copia para nao gerar duplicidade
teste[0]='Maria' ##adiciona maria no teste e consequentemente na galera
teste[1]= 22
galera.append(teste[:]) ##adiciona novamente
print(galera)
