def exibir_mensagem():
    print("olá mundo!")
    
def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}")
    
def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}")
    
exibir_mensagem()
#exibir_mensagem_2() Erro, pois não há parâmetro necessário
exibir_mensagem_2(nome="Jonathan")
exibir_mensagem_3()
exibir_mensagem_3(nome="Jonathan")
