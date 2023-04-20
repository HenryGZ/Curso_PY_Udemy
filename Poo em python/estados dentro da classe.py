#manter estados dentro de classe em poo
#o objeto guarda informações que podem ser
#manipulados e alterados no decorrer do programa

class Camera:
    
    def __init__(self, nome, filmando = False):
        self.nome = nome
        self.filmando = filmando
    
    def filmar(self):
        
        if self.filmando:#verifica se já está filmando para não executar novamente a ação
            print(f'{self.nome} já está filmando')
            return #sai da classe e interrompe a execução do resto 
        
        print(f'{self.nome} está filmando...')
        self.filmando = True
        
    def parar_filmar(self):
        
        if not self.filmando:#verifica se já está filmando para não executar novamente a ação
            print(f'{self.nome} não está filmando')
            return #sai da classe e interrompe a execução do resto 
        
        print(f'{self.nome} finalizando gravação')
        self.filmando = False
    
    
    def fotografar(self):
        
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando')
            return
        
        print(f'{self.nome} está fotografando')
        self.fotografar = True

c1 = Camera('canon')
c2 = Camera('sony')

c1.filmar() #adiciona filmando = True e guarda esse estado
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()

print(c1.filmando)
print(c2.filmando)