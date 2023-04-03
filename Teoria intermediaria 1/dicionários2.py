'''
manipulando dicionários
'''

#criando nova chave dentro de um dicionário
pessoa = {}
pessoa['nome'] = 'teste'
print(pessoa['nome'])

#chave dinamica
teste = {}
chave = 'nome'
teste[chave] = 'pao'
print(teste[chave])

#deletando um valor dentro de um dicionário
apagar = 'sobrenome'
teste[apagar] = 'Dias'
print(teste[apagar])
del teste[apagar]

try:
    (print(teste[apagar]))
except:
    print('chave deletada')
    
