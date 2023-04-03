#contar quantas vezes cada letra apareceu nessa frase:

frase = 'O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido Van Rossum'.upper().replace(' ', '')
print(frase)
mais_vezes = 0
letra = ''
i = 0

while i < len(frase):
    letra_atual = frase[i]
    #if letra_atual == ' ':
        #i+=1
    #else:
    vezes_que_apareceu = frase.count(letra_atual)
    i += 1
    if vezes_que_apareceu > mais_vezes:
        letra = letra_atual
        mais_vezes = vezes_que_apareceu
        
print(f'A letra que mais apareceu foi: {letra} ,e apareceu {mais_vezes} vezes')
    



