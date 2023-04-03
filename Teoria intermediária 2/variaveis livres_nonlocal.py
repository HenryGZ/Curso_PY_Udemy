'''def fora(x):
    a = x # variavel livre
    def dentro():
        return a
    return dentro

dentro1 = fora(10)
dentro2 = fora(20)

print(dentro1())
print(dentro2())'''

def concatenar(string_inicial):
    valor_final = string_inicial
    
    def interna(valor_a_concatenar):
        nonlocal valor_final #indica que a variavel livre vale pra dentro do escopo da função tambem
        valor_final += valor_a_concatenar #essa instrução emite um erro quando sozinha, pois a variavel nao está no escopo da função
        return valor_final
    return interna

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))

    