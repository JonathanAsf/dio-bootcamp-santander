#Parâmetros por nome exemplo:
#Parâmetros posicionais exemplo:
#Parâmetros hibridos

#Misto
#Positional / pode usar keywords 
def criar_carro_position(modelo, ano, placa, /, marca, motor, combustivel):
    print(f"Positional Only:\n{modelo}, {ano}, {placa}, /{marca}, {motor}, {combustivel}")

criar_carro_position("Palio",1999,"ABC-1234",marca="Fiat",motor="1.0",combustivel="Gasolina")
#criar_carro(modelo="Palio",ano=1999,placa="ABC-1234",marca="Fiat",motor="1.0",combustivel="Gasolina") #Inválido pois os primeiros parâmetros são posicionais e foram declarados como keywords

#Keywords only
def criar_carro_keywords(*,modelo,ano,placa,marca,motor,combustivel):
    print(f"Keywords Only:\n{modelo}, {ano}, {placa}, {marca}, {motor}, {combustivel}")

criar_carro_keywords(modelo="Palio",ano=1999, placa="ABC-1234", marca="Fiat", motor=1.0, combustivel="Gasolina") #Válido
#criar_carro("Palio",1999,"ABC-1234",marca="Fiat",motor="1.0",combustivel="Gasolina")#Invpalido

def criar_carro_hibrid(modelo,ano,placa,/,*,marca,motor,combustivel):
    print(f"Hibrid; positional / keywords:\n{modelo}, {ano}, {placa}, {marca}, {motor}, {combustivel}")

criar_carro_hibrid("Palio",1999, "ABC-1234", marca="Fiat", motor=1.0, combustivel="Gasolina") #Válido
#criar_carro("Palio",1999,"ABC-1234",marca="Fiat",motor="1.0",combustivel="Gasolina")#Invpalido