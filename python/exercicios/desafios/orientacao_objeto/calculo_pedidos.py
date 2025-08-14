# Descrição
# Crie uma classe Pedido que represente um pedido em um restaurante, contendo os itens pedidos e um método para calcular o valor total da conta.

# Entrada
# Lista de itens e seus respectivos preços.
# Saída
# O valor total da conta.

class Pedido:
    def __init__(self):
        self.itens = []  
    
    # TODO: Crie um método chamado adicionar_item que recebe um preço e adiciona à lista de itens:
    def adicionar_item (self,preco):        
        # TODO: Adicione o preço do item à lista:
        self.itens.append(float(preco))  

    # TODO: Crie um método chamado calcular_total que retorna a soma de todos os preços da lista:
    def calcular_total(self):
        soma_total = sum(self.itens)
        # TODO: Retorne a soma de todos os preços
        return f"{soma_total:.2f}"

quantidade_pedidos = int(input().strip())

pedido = Pedido()

for _ in range(quantidade_pedidos):
    entrada = input().strip()
    nome, preco = entrada.rsplit(" ", 1)
    #TODO: Chame o método adicionar_item corretamente: 
    pedido.adicionar_item(preco)
# TODO: Exiba o total formatado com duas casas decimais:
print(pedido.calcular_total())
