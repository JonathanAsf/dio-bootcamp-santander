# Descrição
# Uma empresa quer validar se os e-mails cadastrados pelos usuários estão no formato correto. Crie uma função que receba um e-mail e verifique se ele é válido, seguindo as regras:

# 📌 Regras para um e-mail válido:

# Deve conter o caractere "@" e um domínio, como gmail.com ou outlook.com.
# Não pode começar ou terminar com "@".
# Não pode conter espaços.
# Entrada
# Uma string contendo o e-mail a ser validado.
# Saída
# "E-mail válido" se o e-mail estiver no formato correto.
# "E-mail inválido" caso contrário.


# Entrada do usuário
email = input().strip()

# TODO: Verifique as regras do e-mail:

if email.count("@") == 1:
    nome, dominio = email.split("@")

    if nome and dominio and " " not in email and dominio in ["gmail.com", "outlook.com"]:
        print("E-mail válido")
    else:
        print("E-mail inválido")
else:
    print("E-mail inválido")