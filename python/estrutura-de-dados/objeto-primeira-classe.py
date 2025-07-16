#Em python tudo é um onjeto, inclusive funções. Portanto, é possível atribuir funções a variáveis, passá-las como parâmetros para funções, usá-las como valores em estrutura de dados e usar como valor de retorno para uma função


def somar(a,b):
    return a+b

def subtrair(a,b):
    return a-b


def exibir_resultado(a,b,recebe_valores):
    resultado = recebe_valores(a,b)
    print(f"O resultado da operação é = {resultado}")
    
exibir_resultado(20,10,somar)
exibir_resultado(20,10,subtrair)

op = somar

print(f"Ponteiro para função soma, resultado = {op(1,23)}")
