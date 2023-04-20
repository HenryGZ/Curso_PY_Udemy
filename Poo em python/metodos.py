'''
métodos em instancias de classes python

classe - molde (geralmente sem dados)
instancia da classe (objeto) - tem os dados
uma classe pode gerar várias instâncias
na classe o self é a própria instância
'''

class Carro:
    #definir o nome assim na função deixa algo
    #como padrão se nenhum dado for passado
    def __init__(self,nome='sem nome'):
        self.nome = nome
        
    def acelerar(self):
        print(f'{self.nome} está acelerando')




fusca = Carro('fusca')

celta = Carro()#sem nome

print(fusca.nome)
print(celta.nome)

#executando um método dentro da classe
fusca.acelerar()
#ou
Carro.acelerar(fusca)