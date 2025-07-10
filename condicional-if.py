# Estrtura condicional: if

try:
    saldo = 2000.0
    saque = (float(input("Informe o valor que deseja sacar: R$")))
    
    if saldo >= saque:
        print(f"Saque de R$ {saque} realizado com sucesso")
        print(f"Seu saldo atual é de R$ {saldo-saque:.2f}")
    if saldo < saque:
        print("Falha na transação")
        print(f"Você possui R$ {saldo}. Não foi possivel sacar R${saque} por saldo insuficiente")
except:
        print("Erro inesperado. Contate o administrador do sistema.")