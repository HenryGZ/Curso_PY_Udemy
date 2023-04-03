letras = set()
while True:
    letra = input('digite: ')
    letras.add(letra)

    if 'l' in letras:
        print('parabens!!')
        break
    
    print(letras)