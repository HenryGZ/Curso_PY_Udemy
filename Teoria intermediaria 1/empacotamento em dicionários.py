'''
desempacotamento e empacotamento de dicionpários
mais para baixo do código tambem existe exemplo de KWARGS
kwargs = 'keyword arguments'
'''


pessoa = {
    'nome':'Henry',
    'sobrenome':'Goes Zanin',
}
dados_pessoa = {
    'idade':20,
    'altura':1.75,
}

#desempacotamento:
#função values pega retorna os valores das keys
a,b = pessoa
print(pessoa.values())
print('_'*50)

#função items retorna chave e valor
print(pessoa.items())
print('_'*50)

#desempacotamento interno:
(a1,a2),(b1,b2) = pessoa.items()
print(a1,a2)
print(b1,b2)
print('_'*50)

#desempacoptamento com for
for chave,valor in pessoa.items():
    print(chave, valor)
print('_'*50)

#fazer a união de dois dicionários em um só
pessoa_completa = {**pessoa,**dados_pessoa}
print(pessoa_completa)
print('_'*50)

#função para mostrar argumentos nomeados:
def mostro_argumentos_nomeados(*args, **kwargs):
    
    print(f'não nomeados: {args}')
    
    for chave, valor in kwargs.items():
        print(chave, valor)
    
mostro_argumentos_nomeados(1,2,nome = 'joana', exemplo = 123)
print('_'*50)

#desempacotar um dicionário:

mostro_argumentos_nomeados(**pessoa_completa)