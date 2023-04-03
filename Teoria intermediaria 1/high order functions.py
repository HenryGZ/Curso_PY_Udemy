def ola_mundo(msg):
    return msg

#funções funcionam como variáveis
#assim posso dar outro nome a uma função apontando para o endereço
#de memória mas com outro nome

#sem o parenteses para não executar a função
saudacao = ola_mundo

print(saudacao('ola mundo'))

#posso tambem usar uma função apenas para chamar uma ou mais funções

def chama(funcao):
    return(funcao)

print(chama(ola_mundo('ola mundo')))

'''
para nção precisar de falar todos os exemplos apenas deve ficar claro que
UMA FUNÇÃO FUNCIONA COMO UMA VARIÁVEL
'''

#anotação do curso:

'''
Academicamente, os termos Higher Order Functions e First-Class Functions têm significados diferentes.

Higher Order Functions - Funções que podem receber e/ou retornar outras funções

First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

Não faria muita diferença no seu código, mas penso que deveria lhe informar isso.

Observação: esses termos podem ser diferentes e ainda refletir o mesmo significado.
'''