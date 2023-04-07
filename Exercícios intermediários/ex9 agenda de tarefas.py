import os
# Exercício - Lista de tarefas com desfazer e refazer
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

todos = []
desfeitas = []

def adicionar():
    temp = input('informe uma tarefa para ser aficionada: ')
    todos.append(temp)
    menu()

def refazer():
    #o not retorna um booleano e verifica se a lista está vazia
    if not desfeitas:
        os.system("cls")
        print('Não há oque refazer.')
        menu()
    else:
        ultimo = len(desfeitas)
        todos.append(desfeitas[ultimo - 1])
        desfeitas.pop()
        menu()

def desfazer():
    if not todos:
        print('a sua lista já está vazia!')
        menu()
    else:
        ultimo = len(todos)
        desfeitas.append(todos[ultimo - 1])
        todos.pop()
        menu()

def escolha():
    print('informe uma das opções a seguir:')
    print('1 - adiconar')
    print('2 - refazer')
    print('3 - desfazer')
    print('4 - imprimir lista')
    try:
        opcao = int(input('informe uma opção: '))
        return opcao
    except ValueError:
        print('não foi informado um número!!')
        menu()
   
    
def menu():
    #os.system("cls") comando para limpar o console e usa a biblioteca 'os'
    if len(todos) == 0:
        print('__' * 50)
        print('lista vazia')
        print('‾‾' * 50)
    else:
        print('__' * 50)
        print('lista de hoje:\n')
        for c in todos:
            print(c)
        print('‾‾' * 50)
    
    op = escolha()
    int(op)
    opcoes(op)
    
def opcoes(op):
    print(f'dentro da fundao opções{op}')
    if op == 1:
        adicionar()
        menu()
    elif op == 2:
        refazer()
        menu()
    elif op == 3:
        desfazer()
        menu()
menu()