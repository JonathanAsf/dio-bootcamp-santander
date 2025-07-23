#Herança simples ou Unica

class veiculo:
    def __init__(self, placa, cor, numero_rodas):
        self.placa = placa
        self.cor =  cor
        self.numero_rodas = numero_rodas
    
    def ligar_motor(self):
        print("Ligando o motor")
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        
class carro(veiculo):
    pass

class motocicleta(veiculo):
    pass

class caminhao(veiculo):
    def __init__(self,cor,placa,numero_rodas,carregado):
        super().__init__(placa, cor, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f'Sim' if self.carregado else 'Não estou carregado')


moto = motocicleta("abc-1234","preta",2)
carro = carro("asd-0000","vermelho", "4")
caminhao = caminhao("gfd-1234","azul",8,True)

print(moto)
print(carro)
print(caminhao)