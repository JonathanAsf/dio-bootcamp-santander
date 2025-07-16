#Escopo local e Global

#Dentro do bloco da função é local
#Para usar um escopo global, basta usar a palavra reservada "global"
#Não é uma boa prática

salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

print(salario_bonus(500))
