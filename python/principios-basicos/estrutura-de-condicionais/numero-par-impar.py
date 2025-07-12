#Estrutura condicional: Else

try:
    numero = int(input("Digite um número inteiro: "))
    
    if numero % 2 == 0:
        print(f"O número: {numero} é um número par")
    else:
        print(f"O número: {numero} é um número ímpar")

except ValueError:
    print("Você digitou um valor inválido. Por favor, digite um número inteiro.")
