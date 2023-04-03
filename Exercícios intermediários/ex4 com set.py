'''
crie uma função que encontra o primeiro duplicado considerando o sugendo 
numero como a duplicação. Retorne a duplicação considerada.

requisitos: 

    a ordem do numero duplicado é considerada a partir da segunda 
    ocorrencia do número, ou seja, o número dupliicado em si

    exemplo:
    [1,2,3,3,2,1] -> 1,2,3 são duplicados (retorne o numero 2, o primeiro duplicado)

    se não encontrar duplicados na lista, retorne
'''
listas = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

'''
essa função recebe uma lista do for como parametro
nela é definida um set,que não recebe numeros duplicados mas é iterável,
ou seja consigo verificar os numeros dentro dele com o IN
desse modo é verificado cada numero dentro do set e cado ele for igual ao 
que está sendo checado, o laço de repetição é enterrompido
e alterada a resposta para o return
'''
def encontra_duplicados (lista_inteiros):
    resposta = -1#se não houver duplicados a resposta é -1
    numeros_checados = set()#inicia sempre um set vazio

    for numero in lista_inteiros:
            if numero in numeros_checados:
                resposta = numero
                break
            else:
                numeros_checados.add(numero)
    return resposta
     
#o for vai passar a lista a ser analisada e esperar um retorno da função com a resposta
for lista in listas:
    repetido = encontra_duplicados(lista)
    print('='*50)
    print(lista)
    if repetido == -1:
        print(f'não existem numeros duplicados dentro dessa lista')
    else:
        print(f'o primeiro duplicado encontrado é: {repetido}')


