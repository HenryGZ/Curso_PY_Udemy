from functools import partial

# map - para mapear dados
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

def aumentar_porcentagem (valor, porcentagem):
    return round(valor * porcentagem, 2)


#função partial retorna uma closure
aumentar_dez_porcento = partial (
    aumentar_porcentagem,
    porcentagem = 1.1
)

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

#como seria feito a função de mapeamento sem o map
#novos_produtos = [
#   {**p, 'preco': aumentar_porcentagem(p['preco'])} for p in produtos
#]

#com a função map:
def muda_preco_de_produto(produto):
    return {
        **produto,
        'preco': aumentar_dez_porcento(produto['preco'])
        
    }
    
novos_produtos = list(map(muda_preco_de_produto,produtos))
 
print_iter(produtos)
print_iter(novos_produtos)