#args sempre recebe dados no modelo de tupla, separados por virgula
#kwargs sempre recebe dados no modelo de dicionário chave:valor
#args e kwargs são nomes dados por convenção. Pode ser qualquer nome

def exibir_poema(data_extenso, *args,**kwargs):
    texto="\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}"for chave,valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Quarta-feira,16 de julho de 2025","Zen of Python", "Beautiful is better than ugly", author ="Tim petters", ano=1999)

#os valores kwargs só começara a ser alimentado após o primeiro item "chave:valor" ser apresentado