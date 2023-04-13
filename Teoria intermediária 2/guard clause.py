'''
guar clause e evitar o uso de condicionais
usando o exercício de criar tarefas e listas
como exemplo para retirar o uso de if e else dentre
outros tipos de condicionais
'''

'''
trecho de código retirado do material do curso
'''

# while True:
#     print('Comandos: listar, desfazer e refazer')
#     tarefa = input('Digite uma tarefa ou comando: ')


        #esse dicionário lista todas as funções e como elas devem ser chamadas
        #antes de cada função é feita uma função lambda para que seja executada
        #corretamente a função chamada, senão o retorno será sempre none e todas as
        # funções dentro do dicionário seão executadas
#     comandos = {
#         'listar': lambda: listar(tarefas),
#         'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
#         'refazer': lambda: refazer(tarefas, tarefas_refazer),
#         'clear': lambda: os.system('clear'),
#         'adicionar': lambda: adicionar(tarefa, tarefas),
#     }

        #esse é o ódigo que chama as funções corretamente junto com um trecho de código
        #que adiciona um item na lista , ja que no código que foi feito na aula
        #adicionar itens a lista depende de um else
#     comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
#         comandos['adicionar']
#     comando()