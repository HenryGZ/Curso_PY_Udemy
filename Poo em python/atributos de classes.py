class Pessoa:
    ano_atual = 2022# esse atributo vai valer para todas as instancias da classe
    
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade #usando o atributo da classe
                                             #dentro da instancia
    
p1 = Pessoa('joao',35)
print(p1.get_ano_nascimento())
print(Pessoa.ano_atual)#esse atributo salvo na classe pode ser usado fora dela
                       #basta chamar a classe.atributo