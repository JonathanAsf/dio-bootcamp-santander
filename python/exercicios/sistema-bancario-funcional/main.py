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


def efetua_deposito(saldo,valor,extrato):
        
    if valor > 0:
        saldo += valor
        print(f"Operação concluída!")    
    else:
        print("Erro na operação. Não é possível  depositar valores abaixo de zero.")
    
    return saldo


def efetua_saque(*,saldo, valor, numero_saques):     
    if valor > 500:
        print("Erro na operação. Não é possível efetuar valors acima de 500 reais")
    else:             
        if valor > saldo:
            print("Erro na operação. Saldo insuficiente")
        else:
            saldo -= valor
            numero_saques -= 1
            print(f"Operação concluída!")
    return saldo,numero_saques

def exibe_extrato():
    print("Extrato")
    print(f"""
    Saldo atual: R${saldo:.2f}
    Saques disponíveis: {numero_saques}
    """)

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        print("Depósito")
        valor = float(input("Digite o valor que deseja depositar: R$"))
        saldo = efetua_deposito(saldo,valor,extrato)
        
    elif opcao == "s":
        if numero_saques <= 0:
            print("Não é possível fazer saques.\nLimite alcançado de saldos.\nTente Novamente mais tarde.")
        else:
            valor = float(input("Digite o valor que deseja sacar: "))
        
        saldo,numero_saques = efetua_saque(saldo = saldo,valor = valor,numero_saques = numero_saques)
        
    elif opcao == "e":
        exibe_extrato()

    elif opcao == "q":
        print("""
              ################
              Saindo do Sistema
              ################
              """)
        break
    else:
        print(" Operação inválida, por favor seleciona uma opção válida:\n")