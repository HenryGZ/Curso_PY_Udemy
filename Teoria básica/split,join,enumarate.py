'''
função split()
divide uma frase, por exemplo em um carcter definido
'''

frase = 'comi pao com mortadela'
palavras = frase.split(' ')
print(palavras)

'''
função join()
coloca um caracter ou uma frase dentro de uma lista
serve para adicionar caracteres a uma string tambem
'''
frase = ','.join(palavras)
print(frase)

'''
função enumerate
gera indices em tuplas e listas
'''

lista = ['joao','maria','jorge']

for n in enumerate(lista):
    print(n)