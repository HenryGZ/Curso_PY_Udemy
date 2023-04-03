'''
sets são eficientes apra remover dados duplicados de valores iteráveis
os valores são sempre únicos
não aceitam valores mutáveis
não tem indexes
não garantem ordem
são iteraveis(for, in, not in...)
'''

#exemplo de remoção de dados duplicados
l1 = [1,2,3,3,3,3,3,4]
l1 = set(l1)
#convertendo novamente em lista
l1 = list(l1)
print (l1)
#sets apenas aceitam valores imutaveis, não é possivel passar uma lista 
#dentro de um set por exemplo

# exemplo = {[1223]} está comentado mas se colocar pra rodar da erro


'''
o set tambem não possuí indice
por isso a expressão:

l2 = {1,2,3,4}
print(l1[2])

naõ é valida
'''