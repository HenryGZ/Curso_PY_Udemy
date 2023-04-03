lista = []     
while True:
    print('selecione uma das opções: ')
    op = int(input('1 - adicionar\n2 - apagar\n3 - sair\nOpção: '))
    if type(op) != int:
                print('Um numero não foi digitado, tente novamente: ')
                         
    if (op == 1):
        produto = str(input('digite o nome do produto: '))
        lista.append(produto)

    elif(op == 2):
        for i in lista:
            print(lista.index(i)+1, i)
        
        while True:
            #ainda falta fazer a verificação se o item existe na lista
            excluir = int(input('informe o numero do item que deseja excluir: '))
            if type(excluir) != int:
                print('informe um número!!')
            else: 
                break;
        excluir = excluir - 1
        lista.pop(excluir)
        print(lista)
    elif(op == 3):
        print('saindo...')
        break
    #falta fazer a impressão da lista quando sair e limpar o console
    else:
        print('informe um numero valido!!')