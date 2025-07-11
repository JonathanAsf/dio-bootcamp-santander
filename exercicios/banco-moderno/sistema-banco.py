menu = """
Bem vindo ao sistema de bancos mais moderno do País!
Para prosseguir digite uma das opção abaixo

[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair

=>"""
deposito = 0
saldo = 0
limite = 500 
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        print("Depósito")
        saldo += float(input("Digite o valor que deseja depositar: "))
        print(f"Operação concluída!")
    
    elif opcao == "s":
        print("Saque")
        saldo -= float(input("Digite o valor que deseja sacar: "))
        numero_saques += 1
        print(f"Operação concluída!")
        
    elif opcao == "e":
        print("Extrato")
        print(f"""
        Saldo atual: {saldo:.2f}
        Saques disponíveis hoje: {numero_saques}
              """)
    elif opcao == "q":
        print("""
              ################
              Saindo do Sistema
              ################
              """)
        break
    else:
        print(" Operação inválida, por favor seleciona uma opção válida:\n")