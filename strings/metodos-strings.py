#
print("Bem vindo ao sistema de tratamento de texto")
print("Este primeiro modelo transformara o case do seu texto\nExemplo: variavel = python")

exemploCase = "python"
print("variavel.upper() = " + exemploCase.upper())
print("variavel.lower() = " + exemploCase.lower())
print("variavel.title() = " + exemploCase.title())

praticaCase = input("Digite um texto para ser tradado: ")
print(f"Utilizando método upper no texto: {praticaCase.upper()}")
print(f"Utilizando método lower no texto: {praticaCase.lower()}")
print(f"Utilizando método title no texto: {praticaCase.title()}")

#retirar espaços com Strip
print("Este segundo modelo exemplifica a utilização do método strip para retirar excesso de espaços")
print("Exemplo:   Python    ")
exemploStrip = "   Python   "
print("variavel.strip() = " +exemploStrip.strip())
print("variavel.lstrip() = " +exemploStrip.lstrip())
print("variavel.rstrip() = " +exemploStrip.rstrip())

praticaStrip = input("Digite um texto com espaços extras no inicio e no fim para testar os métodos strip: ")
print(praticaStrip.strip()) #remove espaços extras do texto
print(praticaStrip.lstrip())#Remove espaços da esquerda
print(praticaStrip.rstrip()) #Remove espaços da direita

