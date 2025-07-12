#Coleção de objetos com elementos únicos
#Elimina valores duplicados
numeros = set ([1,2,3,1,3,4])
fruta = set("abacaxi")
carros = set(("palio","gol","celta","palio","gol"))
print(numeros)
print(fruta)
print(carros)

numeros = list(numeros)# Não é possível acessar set's sem transformar em lista ou utilizando for
print(numeros[0])

for carro in carros:
    print(carro)

for i, carro in enumerate(carros):
    print(f"{i}: {carro}") 