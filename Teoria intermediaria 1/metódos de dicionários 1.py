'''
len - informa quantas chaves existem
keys - iteráveis com chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor de achave não existe
'''

pessoa = {
    'nome' : 'Luiz Otávio',
    'sobrenome' : 'Miranda'
}

print(len(pessoa))

print(pessoa.keys())
#para usar os valores retornados da função keys é possivel
#transforma-la em uma lista:
print(list(pessoa.keys()))

print(pessoa.values())

#informa a chave e o valor
print(pessoa.items())

#define idade e se não existir ela recebe o valor que foi especificado
pessoa.setdefault('idade', None)
print(pessoa['idade'])




