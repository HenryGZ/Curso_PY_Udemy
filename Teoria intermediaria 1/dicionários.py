'''
dicionários em python (tipo dict)]
dicionários são estruturas de dados do tipo
par de "chave" e "valor
chaves podem ser consideradas como o "indice"
que vimos na lista e podem ser tipos imutáveis
como: str, int, float, bool, tuple, etc...
o valor pode ser de qualquer tipo, incluindo outro
dicionários.
usamos as chaves {} ou a classe dict para declarar um 
dicionário.

imutaveis: str, int, float, bool, tuple
mutaveis: dict, list

exemplo de dicionário:
'''
pessoa = {
    'nome': 'luiz otavio',
    'sobrenome:': 'miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'awdasdawdsd', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ]
}

#o dicionário tambem pode ser declarado da seguinte forma: 
#teste = dict()


print(pessoa, type(pessoa))
print(pessoa['nome'])
