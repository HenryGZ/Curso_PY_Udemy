print('validador de CPF')

cpf = str(input('informe seu CPF: '))

soma = []
c = 10

#metodo replace troca um caracter específico de uma string
#replace('old value', 'new value')
cpf = cpf.replace('.', '')
cpf = cpf.replace('-', '')

#verificação do primeiro dígito:
#contagem regressiva de 10 a 2
for i in range (0,9):
    num = int(cpf[i])
    soma.append(num * c)
    c += -1

digito_1 = sum(soma)

digito_1 = (11 - (digito_1 % 11))

if digito_1 > 9:
    digito_1 = 0


#limpa a lista para eu poder usar o mesmo espaço na memória
soma.clear()

#verificação do segundo dígito:
#contagem regressiva de 11 a 2
c = 11
for i in range (0,9):
    num = int(cpf[i])
    soma.append(num * c)
    c += -1
soma.append(digito_1 * 2)

digito_2 = sum(soma)
digito_2 = (11 - (digito_2 % 11))

v1 = int(cpf[9])
v2 = int(cpf[10])

if (digito_1 == v1 ) and (digito_2 == v2 ):
    print('\ncpf verdadeiro')
else:
    print('cpf falso')
