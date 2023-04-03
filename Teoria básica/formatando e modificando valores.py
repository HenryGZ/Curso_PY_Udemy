'''
:s - formatar strings
:d - formatar inteiros
:f - formatr tipo float

:.(numero)  - quantidade de casas decimais (float)]

:.(caractere)(<,>,^)(quantidade)(tipo: s,d,f)
>   -   esquerda
<   -   direita
^   -   centro
'''


num1 = 1
num2 = 6969
print('_'*10,'a esquerda','_'*10)
print(f'{num1:.>10}')
print(f'{num1:0>10}')

print(f'\n{num2:.>10}')
print(f'{num2:0>10}')
print(f'{num2:^10}')

#o 10 depois do sinal diz quantos caacteres no máximo irá ter
#então sempre aparecerão 10 caracteres

print('_'*10,'ao meio','_'*10)
print(f'{num1:.^10}')
print(f'{num1:0^10}')

print(f'\n{num2:.^10}')
print(f'{num2:0^10}')
print(f'{num2:^10}')

print('_'*10,'a direira','_'*10)
print(f'{num1:.<10}')
print(f'{num1:0<10}')

print(f'\n{num2:.<10}')
print(f'{num2:0<10}')
print(f'{num2:^10}')

'''
tambem funciona com strings, armazenar valores formatados dentro de variaveis
ou apenas imprimilos na tela formatados 
'''

