#parametros mutaveis em python quando adicionados
#em uma função deve ser declarados anteriormente
#ou de uma maneira mais correta com verificação
#se uma lista já foi criada se não deve ser criada

#forma incorreta:

'''
def adiciona_cliente(nome, lista=[]:
    lista.append(nome)
    return lista
''' 

#dessa maneira quando a função for chamada
#caso não for passada uma lista em específico
#haverá apenas a continuação da lista já
#criada dentro da função quando ela foi definida

#para contornar esse problema existem duas formas
#a primeira é declarar uma lista fora da função
#e passar a lista criada como parâmetro:

'''
def adiciona_cliente(nome, lista=[]:
    lista.append(nome)
    return lista

lista1 = []
cliente1 = adiciona_cliente(nome,lista1)
'''

#a segunda maneira de contornar o problema é:
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista
#dessa forma toda vez será criada uma nova lista
#e assim uma lista não afetará outras dentro 
#do programa

