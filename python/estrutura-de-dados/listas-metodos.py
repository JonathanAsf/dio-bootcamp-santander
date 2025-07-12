print("Metodos string")
#Append
print("\nMétodo append\n")
lista = []
lista.append(1)
lista.append("Python")
lista.append([40,30,20])

print(lista)
backupLista = lista.copy()

#Clear
print("\nMétodo clear\n")
print(backupLista)
backupLista.clear()
print(backupLista)

#count
print("\nMétodo count\n")
cores = ["vermelho", "azul", "verde", "azul"]

print(f"Quantidade de 'vermelho' na lista: {cores.count("vermelho")}")
print(f"Quantidade de 'azul' na lista: {cores.count("azul")}")
print(f"Quantidade de 'verde' na lista: {cores.count("verde")}")

#extend
print("\nMétodo extend")
print(cores)
print(lista)
cores.extend([lista])
print(cores)

#index
#retorna a primeira ocorrencia
print("\nMetodo Index")
linguagens = ["python","js","c","java","csharp"]
print(linguagens)
linguagens.index("java")
linguagens.index("python")

#pop
#remove o ultimo elemento da lista ou um indice
print("\nMetodo pop")
print("Remove o item da lista pelo indice (ou o ultimo item)")

print(linguagens)
linguagens.pop()
print(linguagens)
linguagens.pop(2)

#remove
print("\nMetodo remove")
print("Remove o item da lista pelo nome")

print(linguagens)
linguagens.remove("js")
print(linguagens)

#sort
print("\nMetodo sort")
lista_compras = ["ketchup","ovo","mostarda","arroz","batata","frango"]
print(lista_compras)
lista_compras.sort() #sorted(lista_compras) -> outra forma de fazer
print(lista_compras)