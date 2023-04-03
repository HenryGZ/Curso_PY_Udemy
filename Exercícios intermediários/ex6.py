'''
# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, *args):
    return funcao(*args)


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)
'''

def soma(x, y):
    return x + y



#def multiplica(x, y):
    return x * y


def criar_funcao(funcao, *args):
    def closure(*args):
        return funcao(*args)
    return closure


soma_com_cinco = criar_funcao((soma, 5))
multiplica_por_dez = criar_funcao(multiplica, 10)