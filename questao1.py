def conv(n):
    return float (n)/(1024**2)
def conv2(t,n):
    return n*100/t
arquivo = open('usuario.txt', 'r')
lista_usuario = [1,2,3,4,5,6]
c = 0
for linha in arquivo:
    linha = linha.strip()
    lista_usuario[c] = linha
    c += 1
sp = []
for a in range(0,6):
    sp.append(lista_usuario[a].split())
arquivo.close()
vetor_numeros = [1,2,3,4,5,6]
soma_mb = 0
for a in range(0,6):
    vetor_numeros[a] = round(conv(sp[a][1]),2)
    soma_mb += vetor_numeros[a]
b = round(soma_mb, 2)
c = round(b/6,2)
vetor_mb_p = [1,2,3,4,5,6]
for a in range (0,6):
    vetor_mb_p[a] = round(conv2(soma_mb,vetor_numeros[a]),2)
arquivo1 = open('relatorio.txt', 'w')
arquivo1.write('ACME Inc.            Uso do espaço em disco pelos usuários\n------------------------------------------------------------\nNr.  Usuário        Espaço ultilizado      % do uso\n\n\n')
arquivo1.close()
a=0
while a < 6:
    arquivo2 = open('relatorio.txt', 'a')
    arquivo2.write('{}    {}      {}MB            {}%\n'.format(a+1,sp[a][0],vetor_numeros[a],vetor_mb_p[a]))
    a+=1
arquivo2.write('\n\n')
arquivo2.write('Espaço total oculpado: {}MB\nEspaço médio oculpado: {}MB'.format(b,c))
arquivo2.close()




