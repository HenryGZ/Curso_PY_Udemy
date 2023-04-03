'''
pegar dados de um iterável, transforma los ou não
e colocar esses dados em outra lista, porem os dois iteráveis
obrigatoriamente tem que ter o mesmo tamanho
'''

lista_mae = [numero for numero in range(0,10)]
lista_mapeada = [2 * numero for numero in range(0,10)]

#print(f'lista mae: {lista_mae}')
#print(f'lista mapeada: {lista_mapeada}')


#mapeamento com list comprehension
produtos = [
    {'nome':'p1','preco': 20},
    {'nome':'p2','preco': 10},
    {'nome':'p3','preco': 30},
]

#novos_produtos = [
    #{**produto, 'preco': produto['preco'] * 1.05}
    #if produto['preco'] > 20 else {**produto}
    #for produto in produtos
#]

#print(novos_produtos)

 #adicionando filtro:
 #                           (filtro)
lista = [n for n in range(10) if n<5]
print (lista)

'''
é possivel usar list comprehension tambem para dados de uma lista, para incluir nela
por exemplo, apenas os dados seguindo uma certa condição
'''
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos if produto['preco'] >10
]

print(novos_produtos)
