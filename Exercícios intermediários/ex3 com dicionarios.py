perguntas = [
    {
        'pergunta':'quanto é 2+2?',
        'opcoes':['1','3','4','5'],
        'resposta': '4'
    }
]

#print(perguntas[0]['pergunta'])
print(perguntas[0]['pergunta'])
#tentativa = str(input(perguntas[0]['opcoes']))
print('as opções são:')
print(perguntas[0]['opcoes'])
escolha = str(input('escolha: '))

if escolha.isdigit():
    if escolha == perguntas[0]['opcoes'][2]:
        print('acertou!!')
    else:
        print('errou!!')
else:
    print('o caracter digitado não é um numero!!')