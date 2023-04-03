'''
convertendo algumas funções comuns em lambda
'''

#função que será chamada para executar as outras funções pra não
#precisar repetir varias vezes a mesma coisa no código

def executa (funcao, *args):
    return funcao(*args)


#função que será transformada em lambda
def soma(x,y):
    return x+y

#função que irá virar lambda tambem
#pode-se observar q é uma closure
def cria_multiplicador(multiplicador):
    def multiplicador(numero):
        return numero * multiplicador
    return multiplica

#________________________________________________LAMBDA_________________________________________________________#

#função soma escrita como função lambda e sendo executada pela função executa
#passando 2 e 3 como parametros a serem somados
print(executa(lambda x,y: x+y, 2,3))


#função closure escrita em lambda
#uma função lambda executa outra função lambda que retorna o multiplicador(2 nesse caso) * o outro parametro
#que será passado na execução da fução
duplica = executa(lambda m: lambda n: n * m, 2)
print(duplica(10))

#é possivel usar *args dentro de funções lambda:
#lembrando *args é um método de empacotamento
print(executa(lambda *args: sum(args),1,2,3,4,5,6,7,8,9,10))



