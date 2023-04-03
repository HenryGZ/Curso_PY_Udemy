hora = input('informe a hora atual: ')

if hora.isdigit():
    hora = int(hora)
    if(0<hora>24):
        print('digite uma hora válida!')
    else:
        if(hora>=18):
            print('boa noite!')
        elif(0<hora<=6):
            print('boa madrugada!')
        elif(6<hora<=12):
            print('bom dia!')
        else:
            print('boa tarde!')
else:
    print(f'o caracter "{hora}" não é valido!')