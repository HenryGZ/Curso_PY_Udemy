#a tupla é um tipo IMUTAVEL, não permite alterações
#declaraçpão de uma tupla:

nomes = 'maria', 'joao', 'jose'
print(type(nomes))

#ou declarando com parenteses

ingredientes = ('farinha', 'ovo', 'leite')
print(type(ingredientes))


#conversões:

numeros = [1,2,3,4,5]
print(type(numeros))

#convertendo em tupla:
numeros = tuple(numeros)
print(type(numeros))

#convertendo novamente em lista:
numeros = list(numeros)
print(type(numeros))