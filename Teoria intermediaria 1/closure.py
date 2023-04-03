"""
closure e funções que retornam outras funções
"""
def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}!'
    return saudar

def segunda_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

s1 = criar_saudacao('bom dia','Luiz')
print(s1())
'''
^
o segundo parenteses faz o python retornar para a função
e verificar o que havia sido guardado dentro da memória
meio que ele tem que lembrar o que estava na memória dentro da função
pra isso ele retorna até a função e faz a leitura dos dados novamente
para exibir na tela o valor
'''


s2 = segunda_saudacao('boa noite')
print(s2('henry'))
'''
aqui a passagem de parametro foi adiada, 
o valor saudacao é sempre fixo porem o segundo valor
nome pode ser alterado em qualquer momento
lembrando que a estrutura da função tambem foi alterada para poder
ser usada dessa maneira, mas apenas nas suas
passagens de parametro
'''

cumprimentar = segunda_saudacao('olá tudo bom?')
print(cumprimentar('pao'))