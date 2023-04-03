print('_'*50,'aplicando a formatação em strings: ','_'*50)

nome = 'henry'
nome_formatado = '{:*^50}'.format(nome)
print('\n',nome_formatado)

nome2 = 'fulano'
print(f'\n{nome2:-^50}')

'''
.upper()    -    todas as letras maiúsculas
.lower()    -    todas as letras minusculas
.title()    -    primeiras letras maiúsculas
'''

'''
as strings em python funcionam como um vetor, portanto cada caracter possui
uma poisição começando do 0 e indo até o final da string
'''

#positivo  '[01234]'
nometeste = 'henry'
#negativo '-[54321]' começa de um numero não do 0 o negativo
print(nometeste[-1])
print(nometeste[1])
'''
no pyrhon tambem existe o fatiamento de strings usando o sinal
de ':', 'inicio:fim'
'''

print(nometeste[1:4])
print(nometeste[:3])
print(nometeste[3:])
print(nometeste[-1])

'''
tambem da para usar isso pulando espeços nas strings 
por exemplo:
'''

abc ='abcdefghiojklmnopqrstuvwxyz'

print(abc[::2])#pulando de dois em dois
print(abc[:8:2])#parando no caracter 8