'''
combinação - ordem nao importa - iterável + tamanho do grupo
permutação - ordem importa
produto - ordem importa e repete valores unicos
'''
from itertools import combinations, permutations, product

pessoas = ['joao', 'joana', 'luiz', 'leticia']

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]

def print_iter(iterator):
    print(*list(iterator),sep ='\n')
    print('____'*30)

print_iter(combinations(pessoas,2))
#print(*list(combinations(pessoas,2)), sep ='\n') 
#possuim um separador com quebra de linha (* e o sep= '\n')
#print de combinação da lista de pessoas, de dois em dois

print_iter(permutations(pessoas,2))

#o asterisco é para desempacotar o conteúdo
#product multiplica em duas listas o numero um de uma lista com todos de outra lista, depois o dois
#e assim por diante, e faz a mesma coisa com listas no python, até obter todos os resultados possiveis
#sem repetição
print_iter(product(*camisetas))

