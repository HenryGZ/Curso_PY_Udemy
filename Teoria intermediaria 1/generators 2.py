#as funções generator tambem funcionam como iteraveis

def generator(n = 0):
    yield 1 #pausa, diferente do return que encerra a função
    print('continuar 1')#continua a partir dessa linha
    yield 2 #pausa
    print('continuar 2')#continua a partir dessa linha
    yield 3 #pausa
    print('acabando')#continua a partir dessa linha
    return 'acabou'

gen = generator(n=0)
for n in gen:
    print (n)