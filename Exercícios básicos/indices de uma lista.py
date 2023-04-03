lista = ['maria', 'helena', 'luiz']

for nome in lista:
    print(lista.index(nome), nome)
    
print('*' * 50) 
#ou

indices = enumerate(lista)

for item in indices:
    print(item)