n = int(input("Digite a quantidade de pessoas que estão na fila: ").strip())

urgentes = []
normais = []

for _ in range(n):
    nome, idade, tipo = input("Digite nome, idade e prioridade do paciente (separe por ',')").strip().split(",")
    idade = int(idade)
    if tipo == "urgente":
        urgentes.append((nome, idade))
    else:
        normais.append((nome, idade))

# Ordenar cada lista por idade decrescente
urgentes.sort(key=lambda x: x[1], reverse=True)
normais.sort(key=lambda x: x[1], reverse=True)

# Concatenar listas
ordem_atendimento = urgentes + normais

# Imprimir resultado
print("Ordem de Atendimento:", ", ".join(p[0] for p in ordem_atendimento))
