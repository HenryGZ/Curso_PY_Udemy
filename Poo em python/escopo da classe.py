'''
Escopo da classe e de métodos da classe

clases tem escopo, o seu namespace
Métodos tambem tem seu namespace, o seu escopo
assim como funções, a não ser que se use o self
que assim faz referencia do namespace para o escopo
da classe em si 

'''
class Animal:
    # nome = 'Leão'

    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def comendo(self, alimento):
        return f'{self.nome} está comando {alimento}'

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)


leao = Animal(nome='Leão')
print(leao.nome)
print(leao.executar('maçã'))