class Cachorro:
    def __init__(self,nome,cor,acordado = True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a classe...")
    
    def latir(self):
        print("AuAu")


def criar_cachorro():
    scoobyDoo = Cachorro("Scooby","Marrom")
    print(scoobyDoo.nome)
        
#scoobyDoo = Cachorro("Scooby","Marrom")

criar_cachorro()


        