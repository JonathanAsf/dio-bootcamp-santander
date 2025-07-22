import textwrap

def menu(): 
    menu ="""
    Bem vindo ao sistema de bancos mais moderno do País!
    Para prosseguir digite uma das opção abaixo

    [nu] - Novo Usuário
    [d] - Depositar
    [s] - Sacar
    [e] - Extrato
    [q] - Sair


    => """
    return input(textwrap.dedent(menu))

def efetua_deposito(saldo,valor,extrato,/):
        
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR${valor:.2f}\n"
        print(f"===Operação concluída!===")    
    else:
        print("@@@Erro na operação. Não é possível  depositar valores abaixo de zero.@@@")
    
    return saldo,extrato

def efetua_saque(*,saldo, valor, extrato,limite, numero_saques, limite_saques):
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques    
    
    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    
    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor de saque excede o limite. @@@")
        
    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
        
    else:
        print("\n@@@ Operação Falhou. O valor informado é inválido. @@@")    
    return saldo,extrato, numero_saques

def exibe_extrato(saldo, /, *, extrato):
    print("=====Extrato=====")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========")

def cria_usuario(usuarios):
    cpf = input("Digite o seu cpf (Somente números): ")
    usuario = filtrar_usuario(cpf,usuarios)
    
    if usuario:
        print("\n@@@ Já existe usuário com esse CPF. @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Digite a sua data de nascimento(dd-mm-aaaa): ") 
    endereco = input("Informe o endereço (logradouro, numero, - bairro - cidade (sigla) estado: ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        
    print("=== Usuário criado com sucesso! ====")    
    return
     
def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados [0] if usuarios_filtrados else None    

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500 
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
    
        opcao = menu()
        
        if opcao == "d":
            print("Depósito")
            valor = float(input("Digite o valor que deseja depositar: R$"))
            saldo, extrato = efetua_deposito(saldo,valor,extrato)
            
        elif opcao == "s":
            valor = float(input("Digite o valor que deseja sacar: "))
            
            saldo, extrato, numero_saques = efetua_saque(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )        
            
        elif opcao == "e":
            exibe_extrato(saldo, extrato = extrato)

        elif opcao == "nu":
            cria_usuario(usuarios)

        elif opcao == "q":
            print("""
                ################
                Saindo do Sistema
                ################
                """)
            break
        else:
            print(" Operação inválida, por favor seleciona uma opção válida:\n")
    
    
    return

main()