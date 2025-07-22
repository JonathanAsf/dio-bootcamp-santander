def processar_reservas():
    # Entrada dos quartos disponíveis
    quartos_disponiveis = set(map(int, input("quartos disponiveis: ").split()))
    
    # Entrada das reservas solicitadas
    reservas_solicitadas = list(map(int, input("reservas solicitadas: ").split()))

    # TODO: Crie o processamento das reservas:
    reservas_confirmadas = []
    reservas_canceladas = []
    
    # TODO: Verifique se cada reserva pode ser confirmada com base na disponibilidade dos quartos:
    
    for quarto in reservas_solicitadas:
        if quarto in quartos_disponiveis:
            reservas_confirmadas.append(quarto)
            quartos_disponiveis.remove(quarto)
        elif quarto not in quartos_disponiveis:
            reservas_canceladas.append(quarto)

    # Saída dos resultados conforme especificação
    print("\nReservas confirmadas:", " ".join(map(str, reservas_confirmadas)))
    print("Reservas recusadas:", " ".join(map(str, reservas_canceladas)))

# Chamada da função principal
processar_reservas()