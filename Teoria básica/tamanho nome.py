nome = str(input('informe seu primeiro nome: '))

tamanho = len(nome)

if tamanho < 4:
    print('seu nome é pequeno')
elif 4 < tamanho<=6:
    print('tamanho normal')
elif tamanho  > 6:
    print('seu nome é grande')