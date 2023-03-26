class Carro:
    def __init__(self,nome = '', placa = '', fabricante = '', modelo = '',
                 cor = ''):
        self.nome = nome
        self.__placa = placa
        self.__fabricante = fabricante
        self.modelo = modelo
        self.cor = cor 

    @property
    def placa(self):
        return self.__placa
        
    @placa.setter
    def placa(self, placa):
        self.__placa = placa
        
    @property 
    def fabricante(self):
        return self.__fabricante
        
    @fabricante.setter 
    def fabricante(self,fabricante ):
        self.__fabricante = fabricante



    def add(self,n,p,f,m,c):
        self.nome = n
        self.__placa = p 
        self.__fabricante = f
        self.modelo = m 
        self.cor = c

    def status(self):
        print(f'{self.nome}')



