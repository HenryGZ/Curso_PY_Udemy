'''
com o for pode-se usar a função range
a função range tem os seguintes parametros
range(inicio,fim,passo)
'''

for c in range(2,11,2):
    print(c)

texto = 'python'
novo_texto=''
for letra in texto:
    if letra == 't':
        novo_texto = novo_texto + letra.upper()
    else:
        novo_texto = novo_texto + letra
print(novo_texto)