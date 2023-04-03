'''
*args é um tipo de empacotamento para
argumentos não nomeados
é um tipo de empacotamento
mas tem o uso para desempacotar o que foi empacotado tambem
'''

x,y,*resto = 1,2,3,4

print(x,y,resto)

#serve para fazer somatórios por exemplo:

def soma(*args):
#args foi usado para não precisar de definir um numero exato de parametros dentro da função
#os numeros recebidos foram empacotados para serem desempacotados dentro do for
    total = 0
    for c in args:
        total += c
    return total

soma_total = soma(1,2,3,4,5,6,7,8,9,10)
print (soma_total)

# é possivel tambem desempacotar uma tupla criada com *args

tupla = 1,2,3,4,5,6,7,8,9,10
print(f'tupla criada: {tupla}')
print('tupla desempacotada: ',*tupla)