'''
@staticmethod (metódos estáticos) não são tão uteis em python

são metodos que estão dentro da classe
mas não tem acesso ao self nem ao cls
em resumo, são funções que existem dentro da sua classe
'''

class Classe:
    @staticmethod
    def função_que_esta_na_classe(*args, **kwargs):
        print('oi', args, kwargs)

#mesma coisa que staticmethod
def funcao(*args, **kwargs):
    print('oi', args, kwargs)

c1 = Classe()
c1.função_que_esta_na_classe(1,2,3)
funcao(1,2,3)
Classe.função_que_esta_na_classe(nomeado = 1)
funcao(nomeado = 1)
