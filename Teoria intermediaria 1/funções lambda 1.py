'''
funções lambda são funções de um linha
não possui return e não possui nome

servem para limpar o código e deixa-lo mais enxuto

o exemplo aqui sera de um dicionário e um for
que fará a ordenação por nomes
'''

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

#função de ordenação(declação da lambda    retorn   oq vai retornar)
'''lista.sort(key=lambda item:item['nome'])

for nome in lista:
    print(nome)
    
essa é a versão com sort, que ordena a própia lista, alterando ela
    '''





#agora a mesma função com sorted, qu faz uma cópia rasa da lista
def exibir(lista):
    for item in lista:
        print(item)
    print('='*50)

ordena_por_nome = sorted(lista, key=lambda item: item['nome'])
ordena_por_sobrenome = sorted(lista, key=lambda item: item['sobrenome'])

exibir(ordena_por_nome)
exibir(ordena_por_sobrenome)