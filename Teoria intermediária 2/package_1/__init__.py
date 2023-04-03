'''
__init__.py

serve para executar algo sempre que o package for executado
'''

#como esse arquivo sempre executa quando o modulo é importado, é possviel importal todos os modulos
#do package quando ele for chamado, fazendo uma  'gambiarra'

from package_1 import * #um dos unicos casos viáveis para importar tudo de um modulo

#print('você importou algo dentro do package')