try:
    a = 10
    b = 0
    c = a/b
#para tratar o erro corretamente deve ser informado ao except o nome do erro que se espera
#nesse caso é esperado o erro de divisão por zero
#fazendo o tratamento correto do erro esperado    
except ZeroDivisionError:
    print('não é possivel dividir por 0')
#exceções são classem em python que representam erros, a cada erro uma nova exceção deve ser tratada
# em um novo except
except (TypeError, IndexError) as error:# o 'as' jogou o erro para dentro de uma variáve
    print('type error + index error')
    print(f'msg: {error}')
    print(f'nome: ', error.__class__.__name__)#indica o nome da classe do erro
except NameError:
    print('a variavel usada não está definida')
except Exception:#erro geral, pode se tratar de qualquer coisa, não específica
    print('erro desconhecido')
    
    