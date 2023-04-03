lista = ['a','b','c','d','e','f','g']
#listas tambem permitem fatiamento como strings

print(lista[0:5])#print lista do elemento na posição 0 até o 5 com passo 1
print(lista[0::2])#print da lista até o final com passo 2
print(lista[6:0:-1])#print da lista de trás pra frente

lista2 = ['h','i','j','k','l']

lista3 = lista + lista2  #junção das listas
print(lista3)

'''
função extend()
faz a junção de listas
'''

lista.extend(lista2)
print(lista)

'''
função append()
insere um valor no final da lista
'''

'''
função insert()
determina uma posição na lista para ser inserido um valor
'''

lista.insert(0,'banana')
print(lista)

'''
função del()
exclui um valor de um determinado indice
'''
del(lista[0])
print(lista)

'''
função pop()
remove o ultimo item da lista
'''
lista.pop()
print(lista)

'''
preencher uma lista com range
'''
numeros = list(range(1,100,2))
print (numeros)

#max   função que mostra o maior valor da lista
print(max(numeros))
#min   função que mostra o menor valor da lista
print(min(numeros))