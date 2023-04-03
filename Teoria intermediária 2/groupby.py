#agrupando valores 
#biblioteca itertools

from itertools import groupby

def print_groupby(grup):
    for chave,grupo in grup:
        print(chave)
        print(list(grupo))
    print('--'*50)

#vai receber a lista de alunos, e vai retornar a key nota
def ordena(aluno):
    return aluno['nota']

letras = ['a','a','a','a','b','c','c','c','d','e','f','f','f']

#gera um iterator
grupo = groupby(letras)

#desempacota o iteraltor
print_groupby(grupo)
# o group by funciona apenas com dados ordenados, portanto é necessário
#usar algum método de ordenação antes de usar o groupby, sort, sorted, etc...

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]


alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)

print_groupby(grupos)