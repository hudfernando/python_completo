#construindo um dicionario, dicionario sao imutaveis
dicionario = {'chave1':1}
#contruindo lista, lista sao mutaveis
lista = [1,2,3,4,5,1,21,3,4]
# construindo tuplas, tuplas sao imutaveis
tupla = (1,2,3,4)
arquivo = open('Consulta.txt')
arquivo.readline()
# contruindo um set (nao permite adicionar valores iguais )
exemplo_de_set = set()
exemplo_de_set.add(1)
exemplo_de_set.add(2)
exemplo_de_set.add(1)
print(exemplo_de_set)
set_lista = set(lista)
print(set_lista)
#comando for
l = [1,2,3,4,5,6,7,8,9,10]
for indice in l:
    print(indice)
#comando while
x = 0
while x < 10:
    print(x)
    if x == 5:
        break
    x += 1
#metodo range() gea uma lista com o tamanho especificado, mais nao e inicializado na memoria
print(list(range(0, 50, 2)))
variavel = range(1,15)
print(variavel[10])
for i in range(0, 10):
    print(i)
#modos de criar lista
lista1 = [i for i in range(0, 30)]
print(lista1)
x = [i for i in range(0,20) if i % 2 == 0] # insere na lista so valores par
print(x)








