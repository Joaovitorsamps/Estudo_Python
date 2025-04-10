#Variável salário está na raiz do programa e deve utilizar "global" para usar na função
#Isso não é uma boa prática e deve ser evitado
salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

salario_bonus(500)