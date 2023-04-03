'''
add
update
clear
discard
'''

s1 = set()
s1.add('Henry')
#metodo add adiciona itens
s1.add(1)
s1.add(2)
print(f'metodo add adiciona itens individuais: {s1}')
print('nota-se que esse metodo tambem ele adiciona cada letra da string de maneira individual')
s1.update('olá mundo')
s1.update(('teste', 2,34))
print(f'o update faz inserção de vários valores: {s1}')
s1.discard(34)
print(f'descarte do numero 34: {s1}')
#faz o descarte de valores, como o indice do valor não é conhecido
#como parametro ele recebe o próprio valor que é imutavel dentro do set
#e faz sua exclusão
s1.clear()
print(f'set limpo com o método clear: {s1}')