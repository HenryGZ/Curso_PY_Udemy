'''
get - obtém uma chave
pop - apaga um item com a chave especificada (del)
popitem - apaga o último item adicionado
update - atualiza um dicionário com outro
'''

pessoa = {
    'nome' : 'Henry',
    'sobrenome' : 'Goes Zanin',
    'idade' : 20
}
print('comando get: ')
print(pessoa.get('nome'))

#o none funciona tipo o comando del porém ele retorna um valor de uma chave antes de exclui-la
#e faz a exclusão da chave e do valor
print('\ncomando pop:')
nome = pessoa.pop('nome')
print(nome)
print(pessoa)

#popitem faz o retorno e a exclusão tambem, porém da ultima chave de um d8icionário
teste = {
    'nome':'pao',
    'sobrenome':'de forma'
}

ultima_chave = teste.popitem()
print('\ncomando popitem')
print(ultima_chave)
print(teste)

#o update atualiza um dicionário, adicionando ou alterando chaves
teste.update({
    #atualiza uma chave
    'nome':'bread',
    #ou cria novas
    'idade': 30
})
print('\ncomando update:')
print(teste)
#o update pode ser escrito de outra forma: 
teste.update(nome='novo valor', sexo='masculino')
print('\noutra forma do update: ')
print(teste)