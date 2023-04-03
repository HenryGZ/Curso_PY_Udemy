
#serve pra diinuir linhas no código tambem
#exemplo:

nome = str(input('qual seu nome?'))

if type(nome) == str:
    print(f'olá {nome}')
else:
    print('voce não digitou nada')

nome2 = str(input('\n\nseu sobrenome: '))
print(nome2 or 'voce não digitou nada')
#faz a checagem e seleciona a primeira que tem o valor verdadeiro não nulo