'''
o primeiro módulo executado se chama __main__
você pode importar o outro módulo inteiro ou parte dele
o python conhece a pasta onde o __main__ está
e as pastas abaixo dele

não reconhece pastas e módulos acima do __main__ por padrão
o python reconhece todos os módulos e pacotes presentes
nos caminhos do sys.path

exemplo:
'''

import modulo_teste

#a importação de apenas alguma coisa específica de um modulo pode ser feita dessa maneira
#from modulo_teste import soma

print(f'variavel importada: {modulo_teste.variavel_modulo}')
print(f'função soma importada do modulo de teste: {modulo_teste.soma(4,6)}')

'''
modulos são singletons, ou seja apenas carregam uma vez durante o código
a menos que seja especificado que ele deve recarregar o modulo informado
com a seguinte sintaxe:

importlib.reload(nome do modulo)
'''