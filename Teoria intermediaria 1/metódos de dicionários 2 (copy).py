'''
copy - retorna uma cópia rasa(shallow copy)
'''

pessoa = {
    'nome' : 'Henry',
    'sobrenome' : 'Goes Zanin',
    'idade' : 20,
    'lista' : [0,1,2,3]
}

'''
em python um valor aponta para o endereço de memoria d eoutro se nao
for copiado, por isso o metodo copy copia para 
outro local da memória, nao alterando o valor original

porém é feita uma copia rasa e cão copia valores mutáveis,
a copia vai apontar para o mesmo local da memoria nesse caso
'''
copia = pessoa.copy()
copia['teste'] = None
copia['lista'][1] = 30
print(f'pessoa:{pessoa}')
print(f'copia:{copia}')
'''
existe um metodo para resolver esse problema,
existe a biblioteca copy que deve ser importada
e suar o metodo copy.deepcopy que faz uma copia
profunda, copiando qualquer dado, deve-se tomar cuidade
com situações que possuem lista com muitos valores
pois o programa vai ficar exponencialmente mais pesado
'''
import copy
copia_completa = copy.deepcopy(pessoa)
copia_completa['lista'][1] = 1000
print(f'\n\npessoa:{pessoa}')
print(f'copia completa:{copia_completa}')

