#count é um iterator sem fim
from itertools import count

c1 = count(10,4) #iteravel e iterator, sem valor começa do zero, a segunda casa é o multiplicador
r1 = range(10,100, 2) #iteravel mas nao iterator, terceira casa é o multiplicador

#print(next(c1))
#print(next(c1))


#loop infinito
for i in c1:
    if i >= 100:
        break
    print(i)

print('--'*80)
for x in r1:
    print(x)
