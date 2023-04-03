# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)


from dados import dados_produtos
from copy import deepcopy

novos_produtos =  [
    
    {**n, 'preco': round(n['preco'] * 1.1, 2)} 
    for n in deepcopy(dados_produtos.produtos)
]   #para cada linha do dicionário altero a chave 'preco', linha por linha e faço uma deepcopy
    #para dentro de novos produtos
     
produtos_ordenados_por_nome = deepcopy(novos_produtos)
produtos_ordenados_por_nome.sort(key=lambda item:item['nome'], reverse=True)

produtos_ordenados_por_preco = sorted(deepcopy(produtos_ordenados_por_nome), key=lambda item:item['preco'])

print(*produtos_ordenados_por_preco, sep='\n')