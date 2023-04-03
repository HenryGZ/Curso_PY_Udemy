'''serve para criar erros com mensagens personalizadas e informar
qual erro personalizado da maneira que achar mais conveniante na tela
exemplo com divisão por zero: '''

def divide(x,y):
    if x == 0:
        raise ZeroDivisionError('nao é possivel dividir por zero personalizado')
        #nesse caso estou apenas redefinindo a mensagem de rum erro que já existe
        #porem poderia colocar outro nome qualquer no lugar de ZeroDivisionError
        # e informar outro tipo de erro
    return y/x

#função não está sendo executada mas serve de exemplo de uma aplicação prática do raise
def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    #verifica se o valor digitado é inteiro ou float
    if not isinstance(n, (float, int)):
        #cria o erro de tipo e mostra uma mensagem personalizada
        raise TypeError(
            f'"{n}" deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado.'
        )
    return True

print(divide(0,4))