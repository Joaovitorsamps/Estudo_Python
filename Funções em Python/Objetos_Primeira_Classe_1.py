def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao, operacao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {operacao} de {a} e {b} = {resultado}")

a = 10
b = 5

# Exibindo o resultado da soma
exibir_resultado(a, b, somar, "soma")

# Exibindo o resultado da subtração
exibir_resultado(a, b, subtrair, "subtração")

op = somar
op1 = subtrair

print(op(1, 20))
print(op1(25, 20))