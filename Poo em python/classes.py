'''
as classes geram novos objetos(instancias)
que podem ter seus próprios 
atributos(dados) e métodos(funções)

os objetos gerados pela classe podem usar seus dados
internos para realizar várias ações

por convenção usa-se PascalCase para nomes de classes
PascalCase(Pascal Case é a prática de escrever 
palavras compostas ou frases de modo que cada
palavra ou abreviatura comece com uma letra 
maiúscula.)


ao se criar uma classe cria-se um molse que gera outros 
objetos e cad aobjeto tem seu próprio 'self' dentro da
classe
'''

class Pessoa:
    #primeiro método de uma classe sempre é o __init__
    #primeiro parametro a ser passado sempre é o self
    #porem quando o método é chamado não se passa o 
    #parametro para ele, pois ele é a própria instancia
    def __init__(self,nome, sobrenome):
        #atribuindo os dados
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('luiz','otávio')
p2 = Pessoa('maria','joana')

print(p1.nome +' '+ p1.sobrenome)
print(p2.nome +' '+ p2.sobrenome)

