'''
união - union(faz a união de sets)
intersecção - intersection(faz a intersecção de itens presentes em ambos os lados)
diferença - itens presentes apenas no set da esquerda
diferença simétrica - itens que não estão presentes em ambos
'''

s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1 | s2 #união de dois sets
s4 = s1 & s2 #intersecção(itens presentes entre ambos os sets)
s5 = s1 - s2 #apenas os itens unicos presentes no set da esquerda
s6 = s1 ^ s2 #diferença simétrica, de itens únicos presentes em ambos os sets

print(f'set 1: {s1}')
print(f'set 2: {s2}')
print(50*'-')
print(f'união de dois sets: {s3}')
print(f'intersecção de dois sets: {s4}')
print(f'diferença de valores presentes apenas no set da esquerda: {s5}')
print(f'diferença simétrica: {s6}')
