import decimal
#essa biblioteca usa outro tipo de dados para corrigir problemas com numeros
#de ponto flutuantes muito grandes e necessitam ser precisos

numero_1 = 0.1
numero_2 = 0.7

numero_3 = numero_1 + numero_2

print(numero_3)

#print(f'{variavel:.numero de casasf(f de float)}')
print(f'{numero_3:.2f}')

#print(função round(variavel, numero de casas))
print(round(numero_3,2))

#usando a biblioteca que corrige os dados para realizar a conta certa
n1 = decimal.Decimal('0.1')
n2 = decimal.Decimal('0.7')
n3 = n1 + n2
print(n3)