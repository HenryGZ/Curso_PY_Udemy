# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']
'''
def zipper (list1,list2):
    menor_indice = min(len(list1), len(list2))
    return [(list1[x],list2[x]) for x in range(menor_indice)]
            
print(zipper(lista1,lista2))'''

#o python possui uma função pronta que faz a mesma coisa porem retorna um iterator, o zip()
#que deve ser iterado com uma função list() ou um for()

print(list(zip(lista1, lista2)))
            