#if-aninhado

conta_normal = True
conta_universitaria = False

saldo = 2000
cheque_especial = 450

saque = (float(input("Informe o valor que deseja sacar: R$")))

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com :sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso de Chque especial!")
        
elif conta_universitaria:
    if saldo >= saque:
        if saldo >= saque:
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente")
      
#Exemplo de if Ternário  
status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")          