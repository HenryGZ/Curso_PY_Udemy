def escolha():
    print('informe uma das opções a seguir:')
    print('1 - adiconar')
    print('2 - refazer')
    print('3 - desfazer')
    
    opcao = int(input('informe uma opção: '))
    return opcao

def teste ():
    print('chegou na função')

def menu():
    op = escolha()
    opcoes(op)
    
    
def opcoes(op):
    while True:
        print(f'dentro da fundao opções{op}')
        if op == 1:
            teste()
            break
    menu()
        
menu()