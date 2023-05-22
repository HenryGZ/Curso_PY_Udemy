'''
métodos de classe + factories
são métodos onde 'self' será 'cls', ou seja
ao ivés de receber a instancia no primeiro parâmetro
receberemos a própria classe
'''

class Pessoa:
    ano =2023
    
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    
    
    '''
    como class method não é necessária a criação de um objeto
    anteriormente, funções que usam esse decorador criam 
    automaticamento o objeto, não necessitando de receber
    parâmetros, podem tambem retornar parametros sempre pré
    definidos em harded code
    '''
    @classmethod
    def metodo_de_classe(cls):
        print('Hey')
        
    @classmethod
    def criar_com_50_anos(cls,nome):
        return cls(nome,50)
    
    @classmethod
    def criar_sem_nome(cls,idade):
        return cls('anonima',idade)

p1 = Pessoa('João', 34)
#print(Pessoa.ano)
#Pessoa.metodo_de_classe()
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa.criar_sem_nome(24)

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
