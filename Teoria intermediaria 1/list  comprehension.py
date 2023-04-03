'''
forma rápida de criar listas 
a partir de iteráveis
'''

print(f'apenas o print de uma lista: {list(range(10))}') #apenas printa a lista 


#uma forma de preencher uma lista tambem é da seguinte forma usando o for:
lista1 = []
for numero in range(0,10):
    lista1.append(numero)
print(f'lista criada com for: {lista1}')


#usando list comprehension:
lista2 = [numero for numero in range (0,10) ]
print(f'usando list comprehension: {lista2}')