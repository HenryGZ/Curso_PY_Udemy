'''
split - divide uma string
join - une strings
'''

frase = 'curso de python, na Udemy'
lista_de_palavras = frase.split()
print(lista_de_palavras)
#ou com parametros
lista_de_frases = frase.split(',')
print(lista_de_frases)

frases_unidas = '-'.join('abc')
print(frases_unidas)

frases_unidas = '-'.join(lista_de_palavras)
print(frases_unidas)