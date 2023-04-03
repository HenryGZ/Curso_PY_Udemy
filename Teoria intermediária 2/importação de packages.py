'''
é possivel criar um package dentro da pasta raiza do programa
e fazer a importação de modulos dentro dela
'''
import package_1.modulo_do_package
#ou
#from package_1 import modulo_do_package
#ou importar somente uma função dentro de um modulo dentro do package
#from package_1.modulo_do_package import soma_do_modulo
#ou fazer a importação de tudo dentro de um package
#from package_1 import *

print(f'teste de imprtação de função soma de um modulo dentro de um package: {package_1.modulo_do_package.soma_do_modulo(2,3)}')

'''
todas as importações feitas no main devem ser relacionadas com o mesmo, mesma pasta, caso o main
importe algum modulo externo que se relacione com algum modulo irmão daquela outra pasta
o programa irá acusar um erro
'''