#__dict__ e vars para atributos de instância

class Pessoa:
    ano_atual = 2022

    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('joão',35)

'''
para deixar anotado:

a variável poderia receber os dados da sequinte forma:

dados = {'nome':'joão', 'idade': 35}

para receber os dados dentro do objeto é necessário desempacota-los
p1 = Pessoa(**dados)
'''

#p1.nome = 'EITA'#alterou o nome de p1

#del p1.nome #deletou o nome de p1
#print(p1.nome)

print(p1.__dict__) #imprime na tela os valores salvos de p1]
print(vars(p1)) # faz a mesma coisa

#pode se alterar esses valores guardados assim:
#adcionando um item e um valor dentro do dicionário
p1.__dict__['outra'] = 'coisa'
print(p1.outra)