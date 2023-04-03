lista_1 = [1,2,3]
lista_2 = [4,5,6]
lista_3 = []

#adicionar uma lista na outra pode ser de duas formas:
lista_3.extend(lista_1)
lista_4 = lista_1 + lista_2

#adiciona lista em outra lista
lista_2.append(lista_3)

print(lista_4)
print(lista_3)
print(lista_2)

#a lista_B apenas para o endereço de memória, portanto 
#se a lista_A for alterada
lista_A = [ 1,2]
lista_B = lista_A

#para realmente copiar deve-se usar o método .copy()
Lista_C = lista_A.copy()
#assim ela é alocada em outro endereço da memória