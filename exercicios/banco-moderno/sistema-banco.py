menu = """
Bem vindo ao sistema de bancos mais moderno do País!
Para prosseguir digite uma das opção abaixo

[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair

=> """

saldo = 0
limite = 500 
extrato = ""
numero_saques = 3
#LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        print("Depósito")
        deposito = float(input("Digite o valor que deseja depositar: R$"))
        
        if deposito <= 0:
            print("Erro na operação. Não é possível depositar valores abaixo de zero.")
            continue
        else:
            saldo += deposito
            print(f"Operação concluída!")
    
    elif opcao == "s":
        if numero_saques <= 0:
            print("Não é possível fazer saques.\nLimite alcançado.\nTente Novamente mais tarde.")
        else:
            saque = float(input("Digite o valor que deseja sacar: "))
            
            if saque > 500:
                print("Erro na operação. Não é possível efetuar saques acima de 500 reais")
            else:
                if saque > saldo:
                    print("Erro na operação. Saldo insuficiente")
                else:

                    saldo -= saque
                    numero_saques -= 1
                    print(f"Operação concluída!")
        
    elif opcao == "e":
        print("Extrato")
        print(f"""
        Saldo atual: R${saldo:.2f}
        Saques disponíveis: {numero_saques}
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