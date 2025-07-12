#Listas válidas, Exemplos
frutas = ["laranja","marca", "uva"]
fruta = [] #pode ser feita vazia
letras = list("Python")
numeros = list(range(10))
carro = ["Feraria","F8",42000,2020,2900,"São Paulo", True]


#Saida
print(frutas)
print(frutas[0])
print(frutas[1])
print(frutas[2])

print(fruta)


#Fatiamento
print(letras)
print(letras[::-1])
print(letras[2:])
print(letras[:2])
print(letras[1:3])
print(letras[0:3:2])
print(letras[::])


#lista aninhada
#Geralmente serve para representar matrizes

matriz = [
    [1,"a",2],
    ["b",3,4],
    [6,5,"c"]
]

print(matriz)
print(matriz [0]) #[1, "a", 2]
print(matriz [0] [0]) # 1
print(matriz [0] [-1]) # 2
print(matriz [-1] [-1]) # "c"

#Função Enumerate
carros = ["gol", "celta", "palio"]

for indice, carro in enumerate (carros):
        print(f"{indice}: {carros}")
        

#metodo append

numeros = [1,30,21,2,9,74,23,10,322]
pares = []
impares = []

for numero in numeros:
    if numeros % 2 == 0:
        pares.append(numeros)
    else:
        impares.append(numeros)

#list comprehension
#valor retornado
#numeros = [1,30,21,2,9,74,23,10,322]
#pares = [numero for numero in numeros if numero % 2 == 0]
#impares = [numero for numero in numeros if numero % 2 != 0]

quadrado = [numero ** 2 for numero in numeros]