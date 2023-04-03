'''
crie funções que duplicam, triplicam e quadriplicam
o numero recebido como paramentro
'''

'''def duplicar (numero):
    return numero*2

def triplicar (numero):
    return numero*3'''

#e assim por diante
#ou
#uma função que recebe dois parametros em sequencia sendo o primeiro
#o multiplicador e depois o numero que será multiplicado

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))