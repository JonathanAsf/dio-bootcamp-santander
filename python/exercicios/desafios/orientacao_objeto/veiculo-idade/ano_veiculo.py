
from datetime import datetime

# Descrição
# Implemente uma classe Veiculo que represente um carro com marca, modelo e ano. 
#Crie um método que verifique se o carro é considerado antigo (mais de 20 anos).

# Entrada
# Marca, modelo e ano do veículo.

# Saída
# "Veículo antigo" se o carro tiver mais de 20 anos.
# "Veículo novo" caso contrário.

class Veiculo:
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
    def verificar_antiguidade(self):
        ano_atual = datetime.now().year
        if (ano_atual-self.ano) > 20:
            return "Veículo antigo"
        else:
            return "Veículo novo"
          
marca = input().strip()
modelo = input().strip()
ano = int(input().strip())

veiculo = Veiculo(marca, modelo, ano)

print(veiculo.verificar_antiguidade())
