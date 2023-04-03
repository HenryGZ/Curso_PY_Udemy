'''
usando argumentos nomeados para o interpretador ignorar a ordem dos dados
e usar os argumentos pré-definidos com nomes
'''

def soma(x,y):
    print(f'x = {x}, y = {y}, soma = {x+y}')
    
soma(1,4)

soma(x = 4, y = 1)