num1 = input('digite um número: ')
num2 = input('digite um numero: ')

try:
    print(float(num1)+ float(num2))
except:
    print('erro na conversão de valores')
#caso os valores digitados não puderem ser convertidos em inteiro/float, ocorrerá um erro
#try(tente) ira rodar o programa, se acontecer algum erro dentro do bloco try
#o programa não irá parar, irá apenas passar para dentro do bloco de except(exceção)