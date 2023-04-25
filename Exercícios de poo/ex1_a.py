'''
salvar a classe em Json

salvar os dados da classe em json

depois criar novamente as instancias
da classe com os dados salvos
faça em arquivos separados
'''
import json

CAMINHO_ARQUIVO = 'ex1_dados.json'

class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('joao', 20)
p2 = Pessoa('Maria', 21)
p3 = Pessoa('fulano', 40)
bd = [vars(p1),vars(p2),vars(p3)] #poderia ser __dict__ tambem

def fazer_dump():
    with open (CAMINHO_ARQUIVO,'w') as arquivo:
        json.dump(bd,arquivo, ensure_ascii= False, indent= 2)

if __name__ == '__main__':
    print('ELE É O __main__')
    fazer_dump()