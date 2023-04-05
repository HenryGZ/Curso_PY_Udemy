'''
open - abrir um arquivo
modos:
r (leitura), w(escrita), x(criação)
a (escreve ao final), b(binario)
t (modo texto), + (leitura e escrita)
context manager - with(abre e fecha)

metodos uteis:
write, read(escrever e ler)
writelines (escrever várias linhas)
seek (move o cursor)
readline (ler linha)
readlines(ler linhas)

os.remove ou unlink - apaga o arquivo
    import os
    os.remove ou os.unlink (caminho do arquivo)
    
os.rename - troca o nome ou move o arquivo
    import os
    os.rename(caminho do arquivo, 'novo_nome.txt')
    
json.dump - gera um arquivos json
json.load
'''

#arquivo  = open(caminho_arquivo, 'modo')
#fazer algo no arquivo
#arquivo.close()

#o uso de duas barras é para o python nao confundir e interpretar a barra de outra forma
#arquivo = open('C:\\Users\\henry\\OneDrive\\Udemy\\Python\\Teoria intermediária 2\\arquivos\\arquivo.txt', 'w')
#arquivo.close()

#tambem é possivel usar o with para abrir e fechar automaticamente o arquivo:
#o 'w+' serve para escrever mais ler
with open('C:\\Users\\henry\\OneDrive\\Udemy\\Python\\Teoria intermediária 2\\arquivos\\arquivo.txt', 'w+') as arquivo:
    arquivo.write('linha 1\n')
    arquivo.write('linha 2\n')
    
    arquivo.writelines(('linha 3\n', 'linha 4\n'))
    
    #função seek usada para mover o cursor dentro do arquivo
    #o cursor do python fica onde a escrita parou
    #portando se mandar ler depois ele nao vai encontrar nada já que o cursor 
    #está depois do que está escrito
    arquivo.seek(0,0) #volta ao inicio do arquivo
    print(arquivo.read())
    print('--'*20)
    
    #há o metodo readlines que le apenas uma linaha por vez
    #mas ele coloca espaço no final, porém é possivel
    #contornar isso usando end='' ou .strip()
    arquivo.seek(0,0)
    print(arquivo.readline(), end='')
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())
    print(arquivo.readline(), end='')
    print('--'*20)
    

#with open('C:\\Users\\henry\\OneDrive\\Udemy\\Python\\Teoria intermediária 2\\arquivos\\arquivo.txt', 'r') as arquivo:
    #print(arquivo.read())
  
#o metodo 'a+' nao recria o arquivo, se o arquivo já existir ele apenas incluirá uma informação
#não habilita a leitura tambem    
with open('C:\\Users\\henry\\OneDrive\\Udemy\\Python\\Teoria intermediária 2\\arquivos\\arquivo_criado_com_a.txt', 'a+') as arquivo_criado_com_a:
    arquivo_criado_com_a.write('linha\n')

