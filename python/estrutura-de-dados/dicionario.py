#Conjunto de não-ordenado de pares chave:valor
pessoa = {"Nome": "Jonathan", "idade": 22}
#pessoa = dict(nome="Jonathan",idade:22)
pessoa["telefone"] = "3333-3333"

contatos = {
    "teste_usuario1@gmail.com": {"nome": "usuario1", "telefone": "3333-3333"},
    "teste_usuario2@gmail.com": {"nome": "usuario2", "telefone": "4444-4444"},
    "teste_usuario3@gmail.com": {"nome": "usuario3", "telefone": "5555-5555"},   
    "teste_usuario4@gmail.com": {"nome": "usuario4", "telefone": "6666-6666", "hierarquia":{"cargo": "gerente"}},   
}

print(contatos["teste_usuario1@gmail.com"]["nome"])
print(contatos["teste_usuario4@gmail.com"]["hierarquia"] ["cargo"])

#iterar dicionario

for chave in contatos:
     print(chave, contatos[chave])
print()
 #usando metodo
for chave, valor in contatos.items():
     print(chave,valor)
