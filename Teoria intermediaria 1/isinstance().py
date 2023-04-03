'''
usado para saber se objeto é de determinado tipo
'''

lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

for item in lista:
    print(item,isinstance(item,set))
    #retorna um print de true para itens do tipo set
    
for item in lista:
    if isinstance(item,(int, float)):
        print(item * 2)
