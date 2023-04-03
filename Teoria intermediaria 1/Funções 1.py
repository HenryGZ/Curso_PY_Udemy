'''
função em python é denomindada def()

IMPORTANTE!!
funções em python por padrão retornam 'none'
'''

#exemplo:

def varios():
    print('varios1')
    print('varios2')
    
varios()

#passagem de parametros:

def calculo(a,b):
    print(f'\n\nsoma = {a+b}')
    
calculo(3,5)

'''
tratando quando um valor não é passado
definindo um valor padrão para o parametro 
caso algum valor não seja passado para a função ele irá usar
o valor que já foi definido ao inves de mostrar um erro
'''
def ola(nome = 'sem nome'):
    print(f'olá {nome}')
    
ola('henry')
ola()
