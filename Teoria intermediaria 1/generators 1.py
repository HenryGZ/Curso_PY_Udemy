#são funções que conseguem pausar uma execução economizando assim memória

import sys

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__
lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))

#mostra o tamanho em bites
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(generator)

# for n in generator:
#     print(n)