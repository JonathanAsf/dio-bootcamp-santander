def calcular_total(numeros):
    return sum(numeros)

def retornar_antecedor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor,sucessor

print(calcular_total([10,20,30,40,50])) #É possível declarar uma lista de numeros, pois será identificado como apenas 1 argumeto. Retorna um int
print(retornar_antecedor_e_sucessor(3)) #Retorna uma Tupla

def sem_retorno_explicito():
    return

print(sem_retorno_explicito()) #None