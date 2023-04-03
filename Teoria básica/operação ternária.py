'''
operação ternária 
<valor> if <condição> else <outro valor>
'''

condicao = 10 == 10
variavel = 'valor' if condicao else 'outro valor'

print (variavel)

#cada valor False o print passa para o próximo valor
print('valor' if True else 'outro valor' if True else 'fim')