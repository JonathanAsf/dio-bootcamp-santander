# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# TODO: Crie um loop para armazenar participantes e seus temas:
for i in range(n):
  
  recebe_input = input()
  input_tratado = recebe_input.strip()
  
  separa_variaveis = input_tratado.rfind(", ")
  
  participantes = input_tratado[:separa_variaveis]
  tema = input_tratado[separa_variaveis +2:]
  eventos.setdefault(tema, []).append(participantes)

# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")