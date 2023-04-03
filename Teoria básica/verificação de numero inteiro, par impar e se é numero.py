num = input('informe um numero: ')

if num.isdigit():
    num = int(num)
    if (num%2 == 0):
        print(f'o numero digitado {num} é inteiro e par')
    else:
        print(f'o numero digitado {num} é inteiro e ímpar')
else:
    print(f'o caracter digitado "{num}" não é um inteiro')