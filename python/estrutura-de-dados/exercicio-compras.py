# Descrição
# Crie um sistema de carrinho de compras que permita adicionar produtos e calcular o valor total da compra.

# Entrada
# Lista de produtos adicionados ao carrinho (cada um com nome e preço).
# Saída
# Lista dos produtos adicionados e o total da compra.
# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.


# Lista para armazenar os produtos e preços
carrinho = []
total = 0.0

# Entrada do número de itens
n = int(input().strip())

# Loop para adicionar itens ao carrinho
for _ in range(n):
    linha = input("Digite o produto e o valor").strip()
    
    # Encontra a última ocorrência de espaço para separar nome e preço
    posicao_espaco = linha.rfind(" ")
    
    # Separa o nome do produto e o preço
    item = linha[:posicao_espaco]
    preco = float(linha[posicao_espaco + 1:])
    
    # Adiciona ao carrinho
    carrinho.append((item, preco))
    total += preco

# TODO: Exiba os itens e o total da compra
for item,preco in carrinho:
    print(f"{item}:R$ {preco:.2f}")
print(f"R: {total}")
