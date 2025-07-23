class Bicicleta:
    def __init__(self,cor,modelo,ano,valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor 
    
    def buzinar(self):
        print("Plim,Plim...")
    
    def parar(self):
        print("Parando Bicicleta...")
        print("Bicicleta parada!")
        pass
    
    def correr(self):
        print("Vrum")
        
        
           
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave,valor in self.__dict__.items()])}"
        
bicicleta_1 = Bicicleta("vermelha","caloi", 2022, 600)
bicicleta_1.buzinar()
bicicleta_1.correr()
