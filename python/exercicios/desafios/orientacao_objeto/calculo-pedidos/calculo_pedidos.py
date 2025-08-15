class Pedido:
    def __init__(self):
        self.itens = []  

    def adicionar_item (self,preco):        

        self.itens.append(float(preco))  

    def calcular_total(self):
        soma_total = sum(self.itens)
        return f"{soma_total:.2f}"

quantidade_pedidos = int(input().strip())

pedido = Pedido()

for _ in range(quantidade_pedidos):
    entrada = input().strip()
    nome, preco = entrada.rsplit(" ", 1)
    pedido.adicionar_item(preco)

print(pedido.calcular_total())
